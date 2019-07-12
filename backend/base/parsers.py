from django.conf import settings
from django.http import QueryDict
from django.utils import six
from djangorestframework_camel_case.util import underscoreize
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FormParser, MultiPartParser, DataAndFiles
from django.http.multipartparser import MultiPartParserError
from django.http.multipartparser import MultiPartParser as DjangoMultiPartParser


class CamelCaseFormParser(FormParser):
    def parse(self, stream, media_type=None, parser_context=None):
        parser_context = parser_context or {}
        encoding = parser_context.get('encoding', settings.DEFAULT_CHARSET)
        data = QueryDict(stream.read(), encoding=encoding)
        return underscoreize(data)


class CamelCaseMultiPartParser(MultiPartParser):
    def parse(self, stream, media_type=None, parser_context=None):
        parser_context = parser_context or {}
        request = parser_context['request']
        encoding = parser_context.get('encoding', settings.DEFAULT_CHARSET)
        meta = request.META.copy()
        meta['CONTENT_TYPE'] = media_type
        upload_handlers = request.upload_handlers
        try:
            parser = DjangoMultiPartParser(meta, stream, upload_handlers, encoding)
            data, files = parser.parse()
            return DataAndFiles(underscoreize(data), files)
        except MultiPartParserError as exc:
            raise ParseError('Multipart form parse error - %s' % six.text_type(exc))
