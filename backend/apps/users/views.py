from datetime import datetime, timedelta

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.contrib.auth.forms import PasswordChangeForm

from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import update_session_auth_hash

from backend.apps.users.models import User, ActivationCode, AssociatedEmail
from backend.apps.users.serializers import UserRegistrationSerializer, UserSerializer, AuthTokenSerializerWithEmail


class RegistrationView(generics.CreateAPIView):
    """
        post:
        ** Создание нового аккаунта с помощью обычной регистрации
        Поля:
        email
        password

        get:
        ** Подтверждение электронной почты с помощью кода активации
        Парметры:
        activation_code
        email

    """

    allowed_methods = ['GET', 'POST', 'OPTIONS']
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserRegistrationSerializer

    def get(self, request, **kwargs):
        if 'activation_code' in request.query_params and 'email' in request.query_params:
            user = User.objects.get_with_code(
                email=request.query_params.get('email'),
                code=request.query_params.get('activation_code')
            )
            if user:
                try:
                    associated_email = user.associated_email.get(email=request.query_params.get('email'))
                    associated_email.confirmed = True
                    associated_email.save()
                except ObjectDoesNotExist:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
                user.email_confirmed = True
                user.save()
                return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'email': serializer.validated_data['email']},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordRecoveryView(APIView):
    """
    get:
    ** запрос на восстановление пароля
    Нужно передать ?email, и если пользователь с таким email существует, то отправляется email,
    если не существует, то возвращается ошибка, что такого пользователя нет.

    post:
    ** восстановления пароля по ссылке
    email - берется из ссылки по которой перешел пользователь
    code - берется из ссылки по которой перешел пользователь
    password - новый пароль
    password_confirm - подверждение нового пароля
    """

    allowed_methods = ['GET', 'POST', 'OPTIONS']
    authentication_classes = ()
    permission_classes = ()

    def get(self, request, *args, **kwargs):
        try:
            user = User.objects.get(email=request.query_params.get('email'))
        except User.DoesNotExist:
            raise Http404
        code = ActivationCode.create(user)
        # TODO: все такие методы вынести в очередь
        code.send_recovery_password_code()
        return Response(status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.get(email=request.query_params.get('email'))
        except User.DoesNotExist:
            raise Http404
        if ActivationCode.objects.filter(code=request.data.get('code'), associated_email__user=user).exists():
            if request.data.get('password') == request.data.get('password_confirm'):
                user.set_password(request.data.get("password"))
                user.save()
                return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class AuthTokenView(generics.GenericAPIView):
    """
    post:
    ** получение токена
    Для получения нужно отправить username и password, ответов возвращается token

    """

    allowed_methods = ['POST', 'OPTIONS']
    authentication_classes = ()
    permission_classes = ()
    serializer_class = AuthTokenSerializerWithEmail

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user'] or request.user
            token, _ = Token.objects.get_or_create(user=user)
            response = Response(
                {settings.TOKEN_AUTH_COOKIE: token.key}, status=status.HTTP_200_OK
            )
            if settings.TOKEN_AUTH_COOKIE:
                expiration = datetime.utcnow() + settings.TOKEN_EXPIRATION_DELTA
                response.set_cookie(
                    settings.TOKEN_AUTH_COOKIE, response.data[settings.TOKEN_AUTH_COOKIE],
                    expires=expiration, httponly=True
                )
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CurrentUserView(APIView):
    """
    post:
    ** удаление токена авторизации

    get:
    ** Возвращает информацию о текущем пользователе
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(UserSerializer(request.user).data)

    def post(self, request, format=None):
        request.user.auth_token.delete()
        Token.objects.filter(user=request.user).delete()
        response = Response(status=status.HTTP_200_OK)
        if settings.TOKEN_AUTH_COOKIE:
            response.delete_cookie(settings.TOKEN_AUTH_COOKIE)
        return response


class AssociateEmailView(APIView):
    """

    get:
    ** Подтверждение почты

    post:
    ** Отправка кода активации на почту
    Если повторный запрос в течение минуты, то ошибка 400
    """

    def get(self, request, *args, **kwargs):
        if 'activation_code' in request.query_params and 'email' in request.query_params:
            try:
                associated_email = AssociatedEmail.objects.get(email=request.query_params.get('email'))
                associated_email.confirmed = True
                associated_email.save()
            except ObjectDoesNotExist:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            associated_email.user.email = User.objects.normalize_email(request.query_params.get('email'))
            associated_email.user.email_confirmed = True
            associated_email.user.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        if request.data.get('email'):
            if ActivationCode.objects.filter(
                    associated_email__user=request.user,
                    associated_email__email=User.objects.normalize_email(request.data['email']),
                    created_date__gte=datetime.now() - timedelta(minutes=1)
            ).exists():
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': 'Повторите попытку позже'})
            code = ActivationCode.create(request.user, email=User.objects.normalize_email(request.data['email']))
            code.send_confirm_code()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ChangeUserPassView(APIView):
    """

    post:
    ** Смена пароля юзера
    принимает обязательные параметры
    - new_password1
    - new_password2
    - old_password
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        form = PasswordChangeForm(request.user, request.data)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
