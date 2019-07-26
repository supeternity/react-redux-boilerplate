from rest_framework import viewsets, filters, generics


from django_filters.rest_framework import DjangoFilterBackend

from backend.base.permissions import ClientAccessPermission

from . import serializers as certification_serializers
from .extra import ClientLinkFilter


class AdminLinkViewSet(viewsets.ModelViewSet):
    filterset_class = ClientLinkFilter

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)

    search_fields = ('uuid', 'key_id', 'shop_name', 'yur_name', 'client_fio', 'email')
    ordering_fields = ('created_dt', 'uuid', 'key_id', 'shop_name', 'yur_name', 'client_fio', 'email', 'actived_to', 'status')

    def get_model(self):
        return self.get_serializer_class().Meta.model

    def get_queryset(self):
        return self.get_model().objects.all()

    def is_detail_page(self):
        return self.lookup_field in self.kwargs

    def get_serializer_class(self):
        if self.request.method == 'POST':
            if self.is_detail_page():
                return certification_serializers.UpdateClientLinkSerializer
            return certification_serializers.CreateClientLinkSerializer
        return certification_serializers.ClientLinkSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context


class ClientUpdateLinkView(generics.RetrieveUpdateAPIView):

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return certification_serializers.UpdateClientLinkSerializer
        return certification_serializers.ClientLinkSerializer

    def get_queryset(self):
        return super().get_queryset().actives()
