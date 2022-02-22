from rest_framework import serializers as s

from clients.models import Client


class ClientSerializer(s.ModelSerializer):
    class Meta:
        model = Client
        fields = 'id', 'phone', 'mobile_code', 'tag', 'time_zone'
