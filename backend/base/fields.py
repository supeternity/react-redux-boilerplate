from django.db import models
from django.utils.encoding import force_text
from django.utils.html import strip_tags


class SafeHtmlCharField(models.CharField):
    """
        При сохранении удаляет все HTML теги из текста, если в поле указан параметр strip=True
    """

    def __init__(self, strip=False, *args, **kwargs):
        self.strip = strip
        super(SafeHtmlCharField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        value = super(SafeHtmlCharField, self).to_python(value)
        if self.strip:
            value = strip_tags(value)
        return force_text(value)


class SafeHtmlTextField(models.TextField):
    """
        При сохранении удаляет все HTML теги из текста, если в поле указан параметр strip=True
    """

    def __init__(self, strip=False,
                 *args, **kwargs):
        self.strip = strip
        super(SafeHtmlTextField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        value = super(SafeHtmlTextField, self).to_python(value)
        if self.strip:
            value = strip_tags(value)
        return force_text(value)
