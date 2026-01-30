from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# Existing list view
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# New CRUD viewset
class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides CRUD operations for the Book model
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
