from rest_framework import viewsets, response

# Create your views here.
from notifications.models import SendingMessages
from notifications.serializers import SendingMessagesDetailSerializer,\
    SendingMessagesSerializer
from rest_framework import status
from django_q.models import Schedule


class NotificationView(viewsets.ModelViewSet):
    serializer_class = SendingMessagesDetailSerializer
    queryset = SendingMessages.objects.prefetch_related('send_notifications')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = SendingMessagesSerializer(queryset, many=True)
        return response.Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = SendingMessagesSerializer(instance)
        return response.Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        job = Schedule.objects.filter(args=kwargs.get('pk')).first()
        job.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)
