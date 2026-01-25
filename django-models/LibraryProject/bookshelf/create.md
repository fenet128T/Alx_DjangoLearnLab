# Create Operation Documentation

# Command to enter the Django shell:
# python manage.py shell

>>> from bookshelf.models import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> print(book)
# Expected Output: 1984