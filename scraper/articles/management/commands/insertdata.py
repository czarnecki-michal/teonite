from django.core.management.base import BaseCommand, CommandError
from articles.models import Author, Article
from articles.scraper import Scraper

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        scraper = Scraper("https://teonite.com/blog/")
        posts = scraper.get_posts()

        for post, author in posts:
            obj, created = Author.objects.update_or_create(
                id=author[0],
                name=author[1]
            )

            obj, created = Article.objects.update_or_create(
                text=post,
                author_id=Author.objects.get(id=author[0])
            )
