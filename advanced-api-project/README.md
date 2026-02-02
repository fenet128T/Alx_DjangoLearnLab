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

## API Testing

Unit tests are written using Django REST Framework's APITestCase.

### What is tested

- CRUD operations for Book endpoints
- Authentication and permission enforcement
- Filtering, searching, and ordering functionality

### How to run tests

```bash
python manage.py test api
```
