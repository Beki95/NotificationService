from django.urls import path, include
from rest_framework import routers

from notifications.views import NotificationView

router = routers.DefaultRouter()
router.register('', NotificationView, basename='notification')

urlpatterns = [
    path('', include(router.urls))
]
