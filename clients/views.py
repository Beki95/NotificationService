from rest_framework import viewsets

# Create your views here.
from clients.models import Client
from clients.serializers import ClientSerializer


class ClientView(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.filter()


client_create = ClientView.as_view({'post': 'create'})
client_update_delete = ClientView.as_view({'patch': 'partial_update',
                                           'delete': 'destroy'})
