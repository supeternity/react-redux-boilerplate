from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from rest_framework import exceptions
from rest_framework.authentication import (
    get_authorization_header, TokenAuthentication
)


class CookieTokenAuthentication(TokenAuthentication):
    """
    Поиск токена либо в заголовке запроса, либо в куках.
    """
    keyword = settings.TOKEN_AUTH_COOKIE or 'Token'

    def authenticate(self, request):
        auth = get_authorization_header(request).split()
        if not auth or auth[0].lower() != self.keyword.lower().encode():
            if (settings.TOKEN_AUTH_COOKIE and
                    settings.TOKEN_AUTH_COOKIE in request.COOKIES):
                # TODO: Добавить проверки на истечение срока кук
                token = request.COOKIES.get(settings.TOKEN_AUTH_COOKIE)
                return self.authenticate_credentials(token)
            return None

        if len(auth) == 1:
            raise exceptions.AuthenticationFailed(_('Invalid token header. No credentials provided.'))
        elif len(auth) > 2:
            raise exceptions.AuthenticationFailed(_('Invalid token header. Token string should not contain spaces.'))

        try:
            token = auth[1].decode()
        except UnicodeError:
            msg = _('Invalid token header. Token string should not contain invalid characters.')
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)
