from relationship_app.models import Author, Book, Library, Librarian



def retrieve_librarian(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian
