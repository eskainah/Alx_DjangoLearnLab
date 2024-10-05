from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date_time = models.DateTimeField()
    location = models.TextField(max_length=250)
    capacity = models.PositiveIntegerField(default=100) 
    current_capacity = models.PositiveIntegerField(default=0) 
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='events')
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
