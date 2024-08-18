from typing import Any
from django.shortcuts import render
from .models import Book, Library 

from django.views.generic import DetailView
# Create your views here.

def bookListView(request):
    books = Book.objects.all()
    context = {'book_List': books}
    return render(request, 'relationship_app/list_books.html', context)

class Liberary_DetailsView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
      