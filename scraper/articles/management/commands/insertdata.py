from django.core.management.base import BaseCommand, CommandError
from articles.models import Author, Article
from articles.scraper import Scraper

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        scraper = Scraper("https://teonite.com/blog/")
        posts = scraper.get_posts()

        count = 0
        for post, author in posts:
            count += 1
            obj, created = Author.objects.get_or_create(
                id = str(count),
                name = author
            )
            obj2, created2 = Article.objects.get_or_create(
                text = post,
                author_id = Author.objects.get(id=count)
            )
