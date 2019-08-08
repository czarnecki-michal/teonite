from django.test import TestCase
from articles.models import Author, Article
from articles.modules import word_counter


class AuthorTestCase(TestCase):
    """
    Tests Author model
    """

    def setUp(self):
        Author.objects.create(id="jondoe", name="Jon Doe")

    def test_author_id(self):
        """
        Tests if author id is correct
        """

        author = Author.objects.get(name="Jon Doe")
        self.assertEqual(author.id, "jondoe")


class CounterTestCase(TestCase):
    """
    Tests word_counter module
    """

    def test_stopwords_removal(self):
        """
        Tests if stowords and punctuation are removed
        """

        sentence = ("As we all know a picture is worth a thousand words."
                    "So we will let the enhanced pictures speak for themselves.")
        result = word_counter.remove_stopwords(sentence)
        without_stopwords = ["know", "picture", "worth", "thousand",
                             "words", "let", "enhanced", "pictures", "speak"]
        self.assertEqual(result, without_stopwords)

    def test_stopwords_type(self):
        """
        Tests if TypeError is raised
        """

        wrong_type = ["test", "type", "error"]
        self.assertRaises(TypeError, word_counter.remove_stopwords, wrong_type)

    def test_map_words(self):
        """
        Tests if number of words are correctly mapped to word
        """

        words = ["know", "picture", "picture", "picture", "let",
                 "enhanced", "enhanced", "pictures", "speak", "speak", "speak"]
        result = word_counter.map_words(words)
        correct = {"know": 1, "picture": 3, "let": 1, "enhanced": 2, "pictures": 1, "speak": 3}
        self.assertEqual(result, correct)

    def test_get_stats_type(self):
        """
        Tests if TypeError is raised
        """

        a_list = ["test", "type", "error"]
        self.assertRaises(TypeError, word_counter.get_stats, a_list)
        self.assertRaises(TypeError, word_counter.get_stats, None)
        correct_type = [Article(text="test", author_id=Author(id="Test Test", name="testtest"))]
        self.assertEqual(word_counter.get_stats(correct_type), {"test": 1})




# class ScraperTestCase(TestCase):
#     def test_object_constructions(self):
#         pass
