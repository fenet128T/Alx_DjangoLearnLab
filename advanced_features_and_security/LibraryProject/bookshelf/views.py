from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm

def form_example_view(request):
    form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # Edit logic here
    return render(request, 'bookshelf/edit_book.html', {'book': book})
   