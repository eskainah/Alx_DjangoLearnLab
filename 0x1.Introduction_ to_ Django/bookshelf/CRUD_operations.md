from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
books = Book.objects.all()
print(list(books))


book = Book.objects.get(title="1984")
print(f"Title: {book.title}, Author: {book.author}, Publication Year: {book.publication_year}")


book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(f"Updated Title: {book.title}")

from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

print(book)