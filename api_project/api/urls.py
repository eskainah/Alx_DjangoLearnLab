from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList
from .views import BookViewSet

router = DefaultRouter()
router.register(r'my-books', BookViewSet)

urlpatterns = [
    path("api/books/", BookList.as_view(), name="book_list"),
    path('api/', include(router.urls)),
]