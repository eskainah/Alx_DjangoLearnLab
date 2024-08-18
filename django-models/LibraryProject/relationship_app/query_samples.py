from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(name):
    author = Author.objects.get(name=name)
    books = Book.objects.filter(author=author)
    return books

def list_books_in_library(library_name):
    
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

def retrieve_librarian(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian
