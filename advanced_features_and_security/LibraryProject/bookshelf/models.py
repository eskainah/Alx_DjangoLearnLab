from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class Book(models.Model):

    title = models.CharField(max_length = 200)
    author = models.CharField(max_length= 100)
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ('can_view','Can view')
            ('can_create','Can create')
            ('can_edit','Can edit')
            ('can_delete','Can delete')
        ]

    def __str__(self):
        return self.title
    
class CustomUser(AbstractUser):
     date_of_birth = models.DateField(null=True, blank=True)
     profile_photo = models.ImageField(upload_to="profile_profile", null=True, blank=True)
    
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError('Email is required!')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self-self._db)
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password)

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

    