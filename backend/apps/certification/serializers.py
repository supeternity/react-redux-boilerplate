from constance import config

from rest_framework import serializers

from . import models as certification_models


class ClientLinkSerializer(serializers.ModelSerializer):
    status_display = serializers.SerializerMethodField()
    cert_template_display = serializers.SerializerMethodField()

    class Meta:
        model = certification_models.ClientLink
        exclude = ('uuid',)
        read_only_fields = ('status', 'user')

    def get_status_display(self, obj):
        return obj.get_status_display()

    def get_cert_template_display(self, obj):
        return obj.get_cert_template_display()


class CreateClientLinkSerializer(ClientLinkSerializer):

    class Meta:
        fields = ('key_id', 'shop_name', 'yur_name', 'client_fio', 'email', 'cert_template', 'status_display', 'cert_template_display')
        model = certification_models.ClientLink

    def create(self, validate_data):
        validate_data['user'] = self.context['user']
        return super().create(validate_data)


class UpdateClientLinkSerializer(ClientLinkSerializer):

    class Meta:
        model = certification_models.ClientLink
        fields = ('status',)
