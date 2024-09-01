from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList
from .views import BookViewSet
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'my-books', BookViewSet)

urlpatterns = [
    path("api/books/", BookList.as_view(), name="book_list"),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]