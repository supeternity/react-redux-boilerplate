from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer, authenticate

from backend.apps.users.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')

    def validate_email(self, value):
        if User.objects.filter(email=value, email_confirmed=True):
            raise serializers.ValidationError('Такой email уже зарегистрирован')
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'phone', 'email_confirmed', 'balance')


class AuthTokenSerializerWithEmail(AuthTokenSerializer):

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                raise serializers.ValidationError('Не удалось войти в систему с предоставленными учетными данными.', code='authorization')

            if user.email_confirmed is False:
                raise serializers.ValidationError("Необходимо подтвердить email адрес.", code='authorization')
        else:
            raise serializers.ValidationError('Необходимо заполнить все поля.', code='authorization')
        attrs['user'] = user
        return attrs
