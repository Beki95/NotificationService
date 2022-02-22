from django.contrib import admin

# Register your models here.
from notifications.models import SendingMessages, Notification


@admin.register(SendingMessages)
class SendingMessagesAdmin(admin.ModelAdmin):
    pass


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    pass
