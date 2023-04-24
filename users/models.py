from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.BooleanField(default=False)

    street = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)

    email = models.EmailField(max_length=100, unique=False, blank=True)
    phone_no = models.CharField(max_length=10, unique=False, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
