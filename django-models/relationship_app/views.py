from django.shortcuts import render
from relationship_app.models import Book, Library, Author, Librarian
from django.views.generic import DetailView
# Create your views here.

def bookListView(request):
    books = Book.objects.all()
    context = {'book_List': books}
    return render(request, 'relationship_app/list_books.html', context)

class Liberary_DetailsView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    