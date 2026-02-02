from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, permissions, filters
#list view retrieving all books
class BookListView(generics.ListAPIView):
    """
    Lists all books with support for:
    - Filtering
    - Searching
    - Ordering

    Public access (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    # Enable filtering, searching, and ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # Filtering fields
    filterset_fields = ['title', 'publication_year', 'author']

    # Search fields (text-based)
    search_fields = ['title', 'author__name']

    # Ordering fields
    ordering_fields = ['title', 'publication_year']

    # Default ordering
    ordering = ['title']


    #detail view retrieving a single book
class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieves a single book by ID.
    Accessible to anyone.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


    #creating view and adding a new book
class BookCreateView(generics.CreateAPIView):
    """
    Creates a new book.
    Only authenticated users can create books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


#update view modifying an existing book
class BookUpdateView(generics.UpdateAPIView):
    """
    Updates an existing book.
    Only authenticated users can update books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

#delete view removing a book
class BookDeleteView(generics.DestroyAPIView):
    """
    Deletes a book.
    Only authenticated users can delete books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
