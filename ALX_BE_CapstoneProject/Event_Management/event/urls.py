from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (register, login_view, home, 
                    EventViewSet, ProfileViewSet)

router = DefaultRouter()
router.register(r'profile', ProfileViewSet, basename='profile')
router.register(r'events', EventViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('', home, name='home'),
]
