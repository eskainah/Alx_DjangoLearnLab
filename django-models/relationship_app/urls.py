from django.urls import path
from .views import bookListView, Liberary_DetailsView

urlpatterns = [
    path('', bookListView, name='list_books'),
    path('', Liberary_DetailsView.as_view(), name='library_detail'),
]
