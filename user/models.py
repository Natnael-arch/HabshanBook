from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    phone = models.PositiveBigIntegerField(null=True, blank=False, default=None)
