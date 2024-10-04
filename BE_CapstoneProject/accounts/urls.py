from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthViewSet, CustomAuthToken

# Create a router and register the AuthViewSet with it.
router = DefaultRouter()
router.register(r'auth', AuthViewSet, basename='auth')

urlpatterns = [
    path('', include(router.urls)), 
]

urlpatterns += router.urls