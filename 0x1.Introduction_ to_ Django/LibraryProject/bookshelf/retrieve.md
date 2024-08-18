book = Book.objects.get(title="1984")
print(f"Title: {book.title}, Author: {book.author}, Publication Year: {book.publication_year}")