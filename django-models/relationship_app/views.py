from django.shortcuts import render
from relationship_app.models import Book
# Create your views here.

def bookListView(request):
    books = Book.objects.all()
    context = {'book_List': books}
    return render(request, 'relationship_app/list_books.html', context)