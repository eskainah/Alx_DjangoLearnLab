from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Book, Author

# Using the standard RequestFactory API to create a form POST request


class BookTestCases(APITestCase):

    def setUp(self):
        client = APIClient()

        # auth
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # self.author = Author.objects.create(name="First Author")
        # self.book = Book.objects.create(
        #     title='First Book', author=self.author, publication_year=2011)

    def test_create_book(self):
        self.author = Author.objects.create(name="Second Author")
        self.book = {
            'title': "Second Book",
            'author': self.author.id,
            'publication_year': 2021
        }
        self.url = reverse('create_book')
        response = self.client.post(
            self.url, self.book)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Book.objects.count(), 1)

        response.data = response.json()  # Parse json response data
        self.assertEqual(response.data['title'], 'Second Book')

    def test_update_book(self):
        self.author = Author.objects.create(name="Updated Author")
        book = Book.objects.create(
            title='My Book', author=self.author, publication_year=2011)

        self.book = {
            'title': "Updated Book",
            'author': self.author.id,
            'publication_year': 2023
        }
        self.url = reverse('book_update', kwargs={'pk': book.id})
        response = self.client.put(self.url, self.book)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Book.objects.get(
            id=book.id).title, self.book['title'])

    def test_delete_book(self):
        self.author = Author.objects.create(name="Author To be deleted")
        self.book = Book.objects.create(
            title='Book to be deleted', author=self.author, publication_year=2011)
        self.url = reverse('book_delete', kwargs={'pk': self.book.id})
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 204)

        self.assertEqual(Book.objects.count(), 0)

    def test_permission(self):
        self.client.logout()

        # try to create a book instance while logged out
        self.author = Author.objects.create(name="logged-out Author")
        self.book = {
            'title': "logged-out Book",
            'author': self.author.id,
            'publication_year': 2024
        }
        self.url = reverse('create_book')
        response = self.client.post(
            self.url, self.book)
        self.assertEqual(response.status_code, 403)