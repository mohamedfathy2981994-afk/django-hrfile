# accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from workfiles.models import maindata

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    natid = models.CharField(max_length=14, unique=True)
    maindata = models.OneToOneField(maindata, on_delete=models.SET_NULL, null=True, blank=True, related_name='user')

    # Add more fields as needed

    def __str__(self):
        return self.username
