from django.urls import path
from .views import list_books, LibraryDetailsView

urlpatterns = [
    path('', list_books, name='list_books'),
    path('', LibraryDetailsView.as_view(), name='library_detail'),
]
