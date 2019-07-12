from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from backend.apps.users.models import ActivationCode


@receiver(post_save, sender=settings.AUTH_USER_MODEL, dispatch_uid='user_signal')
def user_created(created, instance, **kwargs):
    if created:
        if not instance.email_confirmed:
            code = ActivationCode.create(instance)
            code.send_register_code()
        Token.objects.create(user=instance)
