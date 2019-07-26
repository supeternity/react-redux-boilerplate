import uuid
import datetime

from django.db import models

from django.utils.timezone import now

from constance import config


def default_actived_to():
    return now() + datetime.timedelta(hours=config.LINK_DEFAULT_DELTA)


class ClientLinkQuerySet(models.QuerySet):

    def actives(self):
        return self.filter(actived_to__lte=now)


class ClientLink(models.Model):
    NEW, LENK_SEND, WAITING, GOLD_CERT, SILVER_CERT, RETAKE = 0, 10, 20, 30, 40, 50
    STATUSES = (
        (LENK_SEND, 'ссылка отправлена'),
        (WAITING, 'Ожидает проверки'),
        (GOLD_CERT, 'Зачет (Золотой сертификат)'),
        (SILVER_CERT, 'Зачет (Серебряный сертификат)'),
        (RETAKE, 'Пересдача'),
    )
    CERAMIC_CERT, WALLPAPER_CERT, KMZ_CERT = 0, 10, 20
    CERTS = (
        (CERAMIC_CERT, 'Ceramic 3D'),
        (WALLPAPER_CERT, 'Wallpaper 3D'),
        (KMZ_CERT, 'Kerama Marazzi 3D'),
    )
    uuid = models.UUIDField(verbose_name='Link ID', primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    key_id = models.SlugField(max_length=32, verbose_name='Id ключа')
    shop_name = models.CharField(max_length=128, verbose_name='Название магазина')
    yur_name = models.CharField(max_length=128, verbose_name='Юр. Лицо')
    client_fio = models.CharField(max_length=128, verbose_name='Фио продавца')
    email = models.EmailField(max_length=128, verbose_name='E-mail')
    user = models.ForeignKey('users.User', verbose_name='Пользователь', related_name='transactions', blank=False, null=True, on_delete=models.SET_NULL)
    status = models.PositiveSmallIntegerField(verbose_name='Статус', choices=STATUSES, default=NEW)
    cert_template = models.PositiveSmallIntegerField(verbose_name='Шаблон сертификата', choices=CERTS, default=CERAMIC_CERT)
    actived_to = models.DateTimeField(verbose_name='Дата окончания доступа к ссылкe', default=default_actived_to)
    created_dt = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    modified_dt = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)

    class Meta:
        verbose_name = 'Клиентская ссылка'
        verbose_name_plural = 'Клиентские ссылки'
        ordering = ('-created_dt', '-modified_dt')
