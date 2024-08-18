from django.urls import path
from .views import list_books, LiberaryDetailsView

urlpatterns = [
    path('', list_books, name='list_books'),
    path('', LiberaryDetailsView.as_view(), name='library_detail'),
]
