from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    DOB = models.DateField()
    # profilePicture = models.ImageField(upload_to='profile_images/', blank=True)

    def __str__(self):
        return self.user.username


class Music(models.Model):
    name = models.CharField(max_length=64, primary_key=True)
    number_of_parts = models.IntegerField()

class Event(models.Model):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=256)
    start = models.TimeField()
    end = models.TimeField(null=True)
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()

    def __str__(self):
        return self.name
