from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    """
    Модель для создания информации об авторе
    """
    user_name = models.CharField(max_length=20)

    def __str__(self):
        return self.user_name


class Toilet(models.Model):
    """
    Модель для создания информации о туалете
    """
    author = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=200, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    rating = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    user_tg_id = models.CharField(max_length=12, null=True)
    confirmed = models.BooleanField(default=False, null=True)

    def __str__(self):
        return f'{self.address} | {self.address}'
