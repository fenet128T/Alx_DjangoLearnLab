from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token

from api.models import Author, Book


class BookAPITestCase(APITestCase):
    """
    Test suite for Book API endpoints.
    Covers:
    - CRUD operations
    - Authentication & permissions
    - Filtering, searching, and ordering
    """

    def setUp(self):
        """
        Set up test data and authentication.
        This runs before each test.
        """

        # Create a user
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword123"
        )
          # ✅ Login user (session authentication)
        self.client = APIClient()
        self.client.login(
        username="testuser",
        password="testpassword123"
    )
        # Create token for the user
        self.token = Token.objects.create(user=self.user)

        # Authenticate client
        self.client = APIClient()
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {self.token.key}"
        )

        # Create author
        self.author = Author.objects.create(name="Chimamanda Ngozi Adichie")

        # Create books
        self.book1 = Book.objects.create(
            title="Purple Hibiscus",
            publication_year=2003,
            author=self.author
        )

        self.book2 = Book.objects.create(
            title="Half of a Yellow Sun",
            publication_year=2006,
            author=self.author
        )

    # ---------- READ TESTS ----------

    def test_list_books(self):
        """Anyone can retrieve the list of books"""
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_single_book(self):
        """Anyone can retrieve a single book"""
        response = self.client.get(f"/api/books/{self.book1.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Purple Hibiscus")

    # ---------- CREATE TEST ----------

    def test_create_book_authenticated(self):
        """Authenticated users can create a book"""
        data = {
            "title": "Americanah",
            "publication_year": 2013,
            "author": self.author.id
        }

        response = self.client.post("/api/books/create/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        """Unauthenticated users cannot create a book"""
        self.client.credentials()  # remove auth token

        data = {
            "title": "Unauthorized Book",
            "publication_year": 2020,
            "author": self.author.id
        }

        response = self.client.post("/api/books/create/", data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # ---------- UPDATE TEST ----------

    def test_update_book(self):
        """Authenticated users can update a book"""
        data = {
            "title": "Purple Hibiscus (Updated)",
            "publication_year": 2003,
            "author": self.author.id
        }

        response = self.client.put(
            f"/api/books/{self.book1.id}/update/",
            data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Purple Hibiscus (Updated)")

    # ---------- DELETE TEST ----------

    def test_delete_book(self):
        """Authenticated users can delete a book"""
        response = self.client.delete(
            f"/api/books/{self.book2.id}/delete/"
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # ---------- FILTER / SEARCH / ORDER TESTS ----------

    def test_filter_books_by_year(self):
        """Filter books by publication year"""
        response = self.client.get(
            "/api/books/?publication_year=2006"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(
            response.data[0]["title"],
            "Half of a Yellow Sun"
        )

    def test_search_books_by_title(self):
        """Search books by title"""
        response = self.client.get(
            "/api/books/?search=Purple"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_publication_year_desc(self):
        """Order books by publication year descending"""
        response = self.client.get(
            "/api/books/?ordering=-publication_year"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data[0]["publication_year"],
            2006
        )
