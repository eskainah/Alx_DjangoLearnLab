from django.contrib import admin
from .models import Book
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    pass

class BookAdmin(admin.ModelAdmin):
    # Columns to display in the admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters for the author and publication year fields
    list_filter = ('author', 'publication_year')
    
    # Add search functionality for the title and author fields
    search_fields = ('title', 'author')

# Register your models here.
admin.site.register(Book)

admin.site.register(CustomUser, CustomUserAdmin)