from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    DOB = models.DateField()
    # profilePicture = models.ImageField(upload_to='profile_images/', blank=True)

    def __str__(self):
        return self.user.username

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

class PartFormat(models.Model):
    name = models.CharField(max_length=64, primary_key=True)
    part_data = models.CharField(max_length=1024)

    def __str__(self):
        return self.name

class Music(models.Model):
    name = models.CharField(max_length=64, primary_key=True)
    part_format = models.ForeignKey(PartFormat, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = 'Music'

    def __str__(self):
        return self.name

class Request(models.Model):
    name = models.ForeignKey(Music, on_delete=models.CASCADE)
    part = models.CharField(max_length=32)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.user.username} requests: {self.name.name}"
