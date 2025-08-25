
import secrets
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models



# Create your models here.


class User(AbstractUser):
    mobile = models.CharField(max_length=11, verbose_name='تلفن همراه', unique=True)
    username = models.CharField(max_length=100, verbose_name='اسم کاربر',unique=True, blank=True, null=True)

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.get_full_name()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
