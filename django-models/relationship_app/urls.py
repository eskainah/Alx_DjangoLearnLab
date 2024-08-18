from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('', list_books, name='list_books'),
    path('', LibraryDetailView.as_view(), name='library_detail'),
]
