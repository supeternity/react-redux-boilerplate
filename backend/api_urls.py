from django.urls import path, include
from backend.base.views import SettingsViews

extra_patterns = [
    path('settings/', SettingsViews.as_view(), name='settings'),
    path('users/', include('backend.apps.users.api_urls', namespace='users')),
]
