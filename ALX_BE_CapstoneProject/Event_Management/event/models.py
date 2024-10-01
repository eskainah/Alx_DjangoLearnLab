from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
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

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date_time = models.DateTimeField()
    location = models.TextField(max_length=250)
    capacity = models.PositiveIntegerField(default=100)  # Maximum number of attendees
    current_capacity = models.PositiveIntegerField(default=0)  # Current number of registrations
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organizer')
    created_date = models.DateField()
    #category = models.ForeignKey('Category', on_delete=models.CASCADE)
    #is_recurring = models.BooleanField(default=False)
    #recurrence = models.CharField(max_length=20, null=True, blank=True)  # Weekly, Monthly, etc.
    #recurrence_end_date = models.DateField()

    def __str__(self):
        return self.title
"""""
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
"""""

