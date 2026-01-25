from django.contrib import admin
from .models import Book

# Customizing the Admin Interface
class BookAdmin(admin.ModelAdmin):
    # Display these fields in the admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add search capabilities for title and author
    search_fields = ('title', 'author')
    
    # Add filters for the publication year
    list_filter = ('publication_year',)

# Register the model with the custom admin class
admin.site.register(Book, BookAdmin)