from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (CustomUserViewSet,
                    EventViewSet, ProfileViewSet, AuthTokenViewSet)

router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='user')
router.register(r'profile', ProfileViewSet, basename='profile')
router.register(r'events', EventViewSet)
router.register(r'auth-token', AuthTokenViewSet, basename='auth-token')


urlpatterns = [
    path('', include(router.urls)),
]
