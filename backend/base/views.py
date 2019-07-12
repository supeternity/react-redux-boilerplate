from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from social_core.exceptions import MissingBackend
from social_django.utils import load_strategy, load_backend

from constance import config


class BaseSocialAuth(APIView):

    def initialize_request(self, request, backend, *args, **kwargs):
        parser_context = self.get_parser_context(request)

        request.social_strategy = load_strategy(request)
        if not hasattr(request, 'strategy'):
            request.strategy = request.social_strategy

        try:
            request.backend = load_backend(
                request.social_strategy, backend,
                request.build_absolute_uri(f'/social/{backend}/').replace('http', 'https')
            )
        except MissingBackend:
            return Response(
                {'error': 'Неверный backend'},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Request(
            request,
            parsers=self.get_parsers(),
            authenticators=self.get_authenticators(),
            negotiator=self.get_content_negotiator(),
            parser_context=parser_context
        )


class SettingsViews(APIView):

    def get(self, request, format=None):
        """
        Return a dict of all settings.
        """
        return Response({k: getattr(config, k) for k in list(dir(config))})
