from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone_no = models.CharField(max_length=10, unique=True)
    gender = models.BooleanField(default=False)
    USERNAME_FIELD = 'phone_no'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone_no
