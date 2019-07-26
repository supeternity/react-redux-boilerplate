from django.apps import AppConfig


class CertificationConfig(AppConfig):
    name = 'backend.apps.certification'
    verbose_name = 'Сертификация'
    verbose_name_plural = 'Сертификация'

    # def ready(self):
    #     import backend.apps.catalog.signals  # NOQA

