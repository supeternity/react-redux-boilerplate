from django.db.models import Q


import django_filters
from django_filters import rest_framework as filters

from backend.apps.certification import models as certification_models


class ClientLinkFilter(filters.FilterSet):

    class Meta:
        model = certification_models.ClientLink
        fields = {
            'uuid': ['exact'],
            'status': ['exact'],
            'key_id': ['exact'],
            'shop_name': ['icontains'],
            'yur_name': ['icontains'],
            'client_fio': ['icontains'],
            'email': ['icontains'],
        }
