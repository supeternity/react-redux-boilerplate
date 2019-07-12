from django.test import TestCase
from django.db.models import signals
from rest_framework.test import (
    APITestCase, APIRequestFactory, force_authenticate
)


class BaseTestCase(TestCase):
    def disconnect_signals(self):
        signals.post_save.disconnect(
            sender='users.User', dispatch_uid='user_signal'
        )
        signals.post_save.disconnect(
            sender='likes.Like', dispatch_uid='like_signal'
        )
        signals.post_save.disconnect(
            sender='comments.Comment', dispatch_uid='comment_signal'
        )
        signals.post_save.disconnect(
            sender='subscriptions.Subscription', dispatch_uid='subscription_signal'
        )
        signals.post_save.disconnect(
            sender='video.Video', dispatch_uid='video_signal'
        )


class BaseAPITestCase(APITestCase, BaseTestCase):
    user = None
    factory = APIRequestFactory()

    def get_request(self, url, method, *args, **kwargs):
        request = getattr(self.factory, method)(url, *args, **kwargs)
        request.user = self.user
        force_authenticate(request, self.user)
        return request

    def get_nonauth_request(self, url, method, *args, **kwargs):
        request = getattr(self.factory, method)(url, *args, **kwargs)
        return request
