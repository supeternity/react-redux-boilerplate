import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.sites.models import Site
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.db import models
from django.db.models import F


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, email_confirmed=False):
        if not email:
            raise ValueError('Users must have an email')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.email_confirmed = email_confirmed
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.superuser = True
        user.email_confirmed = True
        user.save(using=self._db)
        return user

    def get_with_code(self, email, code):
        try:
            return self.get_queryset().get(
                email=email, associated_email__activation_code__code=code
            )
        except ObjectDoesNotExist:
            pass
        return None

    def get_with_email(self, email):
        try:
            return self.get_queryset().get(email=email)
        except ObjectDoesNotExist:
            pass
        return None


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email', max_length=255, db_index=True, unique=True
    )
    phone = models.CharField(
        verbose_name='Телефон', max_length=20, default=''
    )
    superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    email_confirmed = models.BooleanField(verbose_name='Электронная почта подтверждена', default=False)
    _balance = models.IntegerField(verbose_name='Баланс', default=0)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['id']

    def __str__(self):
        return self.email

    @property
    def is_admin(self):
        return self.superuser

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_social_auth(self, provider):
        try:
            return self.social_auth.get(provider=provider)
        except ObjectDoesNotExist:
            pass
        return None

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        User.objects.select_for_update().filter(pk=self.pk).update(_balance=F('_balance') + amount)
        self.refresh_from_db()


class ActivationCode(models.Model):
    associated_email = models.ForeignKey('AssociatedEmail', related_name='activation_code', on_delete=models.CASCADE)
    code = models.UUIDField(verbose_name='Код активации', default=uuid.uuid4)
    created_date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Код активации'
        verbose_name_plural = 'Коды активации'

    def __str__(self):
        return f'{self.associated_email.email}: {self.code}'

    @classmethod
    def create(cls, user, email=None):
        associated_email, _ = AssociatedEmail.objects.get_or_create(email=email if email else user.email, user=user)
        return cls.objects.create(associated_email=associated_email)

    def send_register_code(self):
        site = Site.objects.get_current()
        email = self.associated_email.email
        code = self.code
        # TODO: Поменять на актуальную ссылку с фронтенда
        email_html = (f'<a href="http://{site}/api/v1/users/registration/?'
                      f'email={email}&activation_code={code}">Ссылка активации</a>')
        send_mail(
            subject='Регистрация',
            message='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            html_message=email_html
        )

    def send_confirm_code(self):
        site = Site.objects.get_current()
        email = self.associated_email.email
        code = self.code
        # TODO: Поменять на актуальную ссылку с фронтенда
        email_html = (f'<a href="http://{site}/register/?'
                      f'email={email}&activation_code={code}">Ссылка активации</a>')
        send_mail(
            subject='Подтверждение email',
            message='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            html_message=email_html
        )

    def send_recovery_password_code(self):
        site = Site.objects.get_current()
        email = self.associated_email.email
        code = self.code
        # TODO: Поменять на актуальную ссылку с фронтенда
        email_html = (
            f'<a href="https://{site}/recovery/?'
            f'email={email}&activation_code={code}">Восстановление пароля</a>'
        )
        send_mail(
            subject='Восстановление пароля',
            message='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            html_message=email_html
        )


class AssociatedEmail(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='associated_email', on_delete=models.CASCADE)
    email = models.EmailField(verbose_name='Email')
    confirmed = models.BooleanField(verbose_name='Подтвержден', default=False)
    created_date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    modified_date = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)

    class Meta:
        verbose_name = 'Ассоциированный email'
        verbose_name_plural = 'Ассоциированные email'
        unique_together = (('user', 'email'),)

    def __str__(self):
        return self.user.email
