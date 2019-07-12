import os
import re
import random
import unidecode
import urllib.request
import base64
from _md5 import md5
from datetime import timedelta
from time import time

from PIL import Image, ImageDraw, ImageFont
from django.conf import settings
from django.core.files.storage import DefaultStorage
from django.core.files.temp import NamedTemporaryFile
from django.utils import timezone
from django.core.files.base import ContentFile
from django.template.defaultfilters import slugify as dj_slugify
from django.utils.encoding import smart_text
from pytils import translit


def generate_upload_name(instance, filename, prefix=None, unique=False):
    """
    Генерация пути загрузки для файлов для полей
        model.FileField
        model.ImageField
    """
    ext = os.path.splitext(filename)[1]
    basedir = os.path.join(instance._meta.app_label, instance._meta.model_name)
    name = str(instance.pk or '') + filename + (str(time()) if unique else '')
    filename = md5(name.encode('utf8')).hexdigest()
    if prefix:
        basedir = os.path.join(basedir, prefix)
    return os.path.join(basedir, filename[:2], filename[2:4], '{}{}'.format(translit.slugify(filename), ext))


def now_plus_30_days():
    return timezone.now() + timedelta(days=30)


def generate_avatar(symbol, size='100x100'):
    image_path = os.path.join(
        settings.MEDIA_ROOT, 'markup', 'images', symbol, 'no_photo.png'
    )
    storage = DefaultStorage()
    if storage.exists(image_path):
        return os.path.join(settings.MEDIA_URL, 'markup', 'images', symbol, 'no_photo.png')
    try:
        if not os.path.exists(os.path.join(settings.MEDIA_ROOT, 'markup', 'images', symbol)):
            os.makedirs(os.path.join(settings.MEDIA_ROOT, 'markup', 'images', symbol))
        geometry = tuple(map(int, size.split('x')))
        img = Image.new('RGB', geometry, (random.randint(30, 200), random.randint(20, 200), random.randint(20, 200)))
        drawer = ImageDraw.Draw(img)
        font = ImageFont.truetype('backend/static/fonts/OpenSans-SemiBold.ttf', size=40)
        drawer.text((15, 10), symbol, font=font)
        img.save(fp=image_path)
        return os.path.join(settings.MEDIA_URL, 'markup', 'images', symbol, 'no_photo.png')[:]
    except Exception:
        return ''


def get_no_photo_url(size='100x100', **options):
    image_path = os.path.join(
        settings.MEDIA_ROOT, 'markup', 'images', size, 'no_photo.png'
    )
    storage = DefaultStorage()
    if storage.exists(image_path):
        return os.path.join(settings.MEDIA_URL, 'markup', 'images', size, 'no_photo.png')
    try:
        print(image_path)
        if not os.path.exists(os.path.join(settings.MEDIA_ROOT, 'markup', 'images', size)):
            os.makedirs(os.path.join(settings.MEDIA_ROOT, 'markup', 'images', size))
        img = Image.open(os.path.join(settings.STATICFILES_DIRS[0], 'img', 'standart-ava3x.png'))
        img.thumbnail(tuple(map(int, size.split('x'))))
        img.save(fp=image_path)
        return os.path.join(settings.MEDIA_URL, 'markup', 'images', size, 'no_photo.png')
    except Exception:
        return None


class TempDisconnectSignal(object):
    def __init__(self, signal, receiver, sender, dispatch_uid=None):
        self.signal = signal
        self.receiver = receiver
        self.sender = sender
        self.dispatch_uid = dispatch_uid

    def __enter__(self):
        self.signal.disconnect(
            receiver=self.receiver,
            sender=self.sender,
            dispatch_uid=self.dispatch_uid,
            weak=False
        )

    def __exit__(self, type, value, traceback):
        self.signal.connect(
            receiver=self.receiver,
            sender=self.sender,
            dispatch_uid=self.dispatch_uid,
            weak=False
        )


def file_from_url(url):
    img_temp = NamedTemporaryFile(delete=True)
    with urllib.request.urlopen(url=url) as response:
        img_temp.write(response.read())
        img_temp.flush()
        return img_temp


def lang_switcher(phrase):
    eng = '~!@#$%^&qwertyuiop[]asdfghjkl;\zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:"|ZXCVBNM<>?'
    rus = 'Ё!"№;%:?йцукенгшщзхъфывапролдж\ячсмитьбю.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,'
    new_phrase = []
    for word in phrase.split(' '):
        new_word = []
        if all([symbol in eng for symbol in word]):
            for symbol in word:
                index = eng.find(symbol)
                new_word.append(rus[index])
            new_phrase.append(''.join(new_word))
        else:
            new_phrase.append(word)
    return ' '.join(new_phrase)


def convert_base64(data):
    file_obj = None
    if isinstance(data, str) and data.startswith('data:image'):
        if data.count(';base64,') == 1:
            frmt, imgstr = data.split(';base64,')
            ext = frmt.split('/')[-1]
            try:
                file_name = f'temp_from_base64__{random.randint(0, 1000)}{random.randint(0, 1000)}.{ext}'
                file_obj = ContentFile(base64.b64decode(imgstr), name=file_name)
            except Exception as e:
                file_obj = None
    return file_obj


def slugify(value):
    return dj_slugify(smart_text(unidecode.unidecode(smart_text(value))))


def unique_slugify(instance, value, slug_field_name='slug', queryset=None, slug_separator='-', return_slug=True):
    """
    Calculates and stores a unique slug of ``value`` for an instance.

    ``slug_field_name`` should be a string matching the name of the field to
    store the slug in (and the field to check against for uniqueness).

    ``queryset`` usually doesn't need to be explicitly provided - it'll default
    to using the ``.all()`` queryset from the model's default manager.
    """
    slug_field = instance._meta.get_field(slug_field_name)

    slug = getattr(instance, slug_field.attname)
    slug_len = slug_field.max_length

    # Sort out the initial slug, limiting its length if necessary.
    slug = slugify(value)
    if slug_len:
        slug = slug[:slug_len]
    slug = _slug_strip(slug, slug_separator)
    original_slug = slug

    # Create the queryset if one wasn't explicitly provided and exclude the
    # current instance from the queryset.
    if queryset is None:
        queryset = instance.__class__._default_manager.all()
    if instance.pk:
        queryset = queryset.exclude(pk=instance.pk)

    # Find a unique slug. If one matches, at '-2' to the end and try again
    # (then '-3', etc).
    next = 2
    while not slug or queryset.filter(**{slug_field_name: slug}):
        slug = original_slug
        end = '%s%s' % (slug_separator, next)
        if slug_len and len(slug) + len(end) > slug_len:
            slug = slug[:slug_len - len(end)]
            slug = _slug_strip(slug, slug_separator)
        slug = '%s%s' % (slug, end)
        next += 1
    if return_slug:
        return slug
    setattr(instance, slug_field.attname, slug)


def _slug_strip(value, separator='-'):
    """
    Cleans up a slug by removing slug separator characters that occur at the
    beginning or end of a slug.

    If an alternate separator is used, it will also replace any instances of
    the default '-' separator with the new separator.
    """
    separator = separator or ''
    if separator == '-' or not separator:
        re_sep = '-'
    else:
        re_sep = '(?:-|%s)' % re.escape(separator)
    # Remove multiple instances and if an alternate separator is provided,
    # replace the default '-' separator.
    if separator != re_sep:
        value = re.sub('%s+' % re_sep, separator, value)
    # Remove separator from the beginning and end of the slug.
    if separator:
        if separator != '-':
            re_sep = re.escape(separator)
        value = re.sub(r'^%s+|%s+$' % (re_sep, re_sep), '', value)
    return value


def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META['HTTP_X_REAL_IP'] if 'HTTP_X_REAL_IP' in request.META else request.META['REMOTE_ADDR']
    return ip


def prepare_phone(phone_number):
    phone_number = ''.join([x for x in str(phone_number) if x.isdigit()])
    if phone_number:
        if phone_number[0] == '8':
            phone_number = ''.join(['7', phone_number[1:]])
    return phone_number
