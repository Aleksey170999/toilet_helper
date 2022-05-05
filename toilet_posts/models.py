from datetime import datetime
from django.utils import timezone
from django.db import models


class Author(models.Model):
    """
    Модель для создания информации об авторе
    """
    first_name = models.CharField(max_length=25, null=True)
    last_name = models.CharField(max_length=25, null=True)
    post_count = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ToiletGallery(models.Model):
    images = models.ImageField(upload_to='images/gallery', blank=True)
    toilet_id = models.ForeignKey('Toilet', on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return str(self.images)


class Toilet(models.Model):
    """
    Модель для создания информации о туалете
    """
    author = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=200, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    rating = models.IntegerField(blank=False, null=False)
    location = models.CharField(max_length=50, blank=False, null=False)
    user_tg_id = models.CharField(max_length=12, blank=False, null=False)
    confirmed = models.BooleanField(default=False, null=False)
    img = models.ImageField(null=True, blank=True, upload_to='images/')
    created_date = models.DateTimeField(null=True, blank=False, default=timezone.now)

    def __str__(self):
        return self.address

