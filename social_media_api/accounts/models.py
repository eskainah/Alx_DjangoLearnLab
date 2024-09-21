from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(max_length=250)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True)
    followers = models.ManyToManyField('self', symmetrical=False)

    def __str__(self):
        return self.username