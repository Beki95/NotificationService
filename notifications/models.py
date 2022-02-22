from django.db import models
from .settings import ChoiceFilter
from django_q.models import Schedule


# Create your models here.
class SendingMessages(models.Model):
    start_date = models.DateTimeField()
    text = models.CharField(max_length=100)
    choice_filter = models.CharField(max_length=10,
                                     choices=ChoiceFilter.choice(),
                                     default=ChoiceFilter.CODE)
    end_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        return super(SendingMessages, self).save(*args, **kwargs)


class Notification(models.Model):
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    sending_message = models.ForeignKey('notifications.SendingMessages',
                                        on_delete=models.PROTECT,
                                        related_name='send_notifications')
    client = models.ForeignKey('clients.Client', on_delete=models.PROTECT,
                               related_name='client_notifications')
