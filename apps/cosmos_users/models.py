from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username    = models.CharField(max_length=255, unique=True)
    email       = models.CharField(max_length=255, unique=True)
    password    = models.CharField(max_length=255)
    name        = None

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'