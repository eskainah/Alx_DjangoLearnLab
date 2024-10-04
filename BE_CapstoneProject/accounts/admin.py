from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CustomUser, Profile
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
   
    fieldsets = UserAdmin.fieldsets 
    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)