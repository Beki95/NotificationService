from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Client(models.Model):
    phone = PhoneNumberField()
    mobile_code = models.IntegerField()
    tag = models.CharField(max_length=10)
    time_zone = models.CharField(max_length=20)
