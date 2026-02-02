## Filtering, Searching, and Ordering

The Book list endpoint supports advanced query features:

### Filtering
- `?publication_year=2006`
- `?author=1`

### Searching
- `?search=hibiscus`
- Searches title and author name fields

### Ordering
- `?ordering=title`
- `?ordering=-publication_year`

These features are implemented using:
- DjangoFilterBackend
- SearchFilter
- OrderingFilter
