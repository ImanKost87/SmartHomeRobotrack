from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class SensorsData(models.Model):
    data = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.data


class SensorsSetup(models.Model):
    setup = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.setup


class UserData(models.Model):
    data = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.data
