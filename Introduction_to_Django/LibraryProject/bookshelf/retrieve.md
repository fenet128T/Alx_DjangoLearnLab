# Retrieve Operation
python manage.py shell

>>> from bookshelf.models import Book
>>> books = Book.objects.all()
>>> for book in books:
>>>     print(book.title, book.author, book.publication_year)
# Output: 1984 George Orwell 1949