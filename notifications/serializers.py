from rest_framework import serializers as s

from notifications.jobs import ScheduledTask
from notifications.models import SendingMessages, Notification

from notifications.services import Mailing
from notifications.settings import ChoiceFilter
from datetime import datetime
import pytz
from typing import Dict


class NotificationSerializer(s.ModelSerializer):
    class Meta:
        model = Notification
        fields = 'id', 'status', 'sending_message', 'client'


class SendingMessagesDetailSerializer(s.ModelSerializer):
    start_date = s.DateTimeField()
    end_date = s.DateTimeField()
    choice_filter = s.ChoiceField(choices=ChoiceFilter.choice())

    class Meta:
        model = SendingMessages
        fields = 'id', 'start_date', 'text', 'choice_filter', 'end_date'

    def create(self, validated_data):
        send_messages = super().create(validated_data)
        creating_mailing(validated_data, send_messages)
        return validated_data


class SendingMessagesSerializer(SendingMessagesDetailSerializer):

    def to_representation(self, instance):
        data = super().to_representation(instance)
        query = instance.send_notifications.order_by('status')
        data['notifications'] = NotificationSerializer(query, many=True).data
        return data


def creating_mailing(attrs: Dict, obj: SendingMessages) -> None:
    start_date = attrs.get('start_date')
    end_date = attrs.get('end_date')
    now = datetime.now(pytz.UTC)
    if (start_date < now) and (end_date > now):
        # сразу всем отправить
        Mailing.request(pk=obj.id)
    elif start_date > now:
        # создать рассылку
        task = ScheduledTask(obj_id=obj.id)
        task.create_scheduled_task()
