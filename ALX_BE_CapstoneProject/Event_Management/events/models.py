from django.contrib.auth.models import AbstractUser 
from django.db import models

#create a Custom user model
class CustomUser(AbstractUser):
    middle_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)

    # Override the username field to ensure it's unique
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"