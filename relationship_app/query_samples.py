from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)


# List all books in a library
def query_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()


# Retrieve the librarian for a library
def query_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)
