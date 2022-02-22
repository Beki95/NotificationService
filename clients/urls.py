from django.urls import path
from .views import client_update_delete, client_create

urlpatterns = [
    path('', client_create),
    path('<int:pk>/', client_update_delete)
]
