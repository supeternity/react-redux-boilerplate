"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .api_urls import extra_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(extra_patterns)),
]

admin.site.site_header = "alpaca Admin"
admin.site.site_title = "alpaca Admin Portal"
admin.site.index_title = "Welcome to alpaca Portal"

if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static
    from rest_framework_swagger.views import get_swagger_view

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_ROOT, document_root=settings.STATIC_ROOT)

    swagger_view = get_swagger_view(title='alpaca API')
    urlpatterns.append(path('staff/swagger/', swagger_view),)

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
