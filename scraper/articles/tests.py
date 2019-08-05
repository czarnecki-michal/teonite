from django.test import TestCase
from articles.models import Author


class AuthorTestCase(TestCase):
    def setUp(self):
        Author.objects.create(id="jondoe", name="Jon Doe")

    def test_author_id(self):
        author = Author.objects.get(name="Jon Doe")
        self.assertEqual(author.id, "jondoe")
