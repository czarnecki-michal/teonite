import logging

from django.core.management.base import BaseCommand

from scraper.articles.modules.scraper import Scraper
from scraper.articles.models import Article, Author

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class Command(BaseCommand):
    help = 'Inserts scraped data from blog into database'

    def handle(self, *args, **options):
        scraper = Scraper("https://teonite.com/blog/")
        posts = scraper.get_posts()

        logger.info("Updating %s articles.", len(posts))
        new_articles = 0
        new_authors = 0
        for post, author in posts:
            _, created = Author.objects.update_or_create(
                id=author[0],
                name=author[1]
            )
            if created:
                new_authors += 1
            _, created = Article.objects.update_or_create(
                text=post,
                author_id=Author.objects.get(id=author[0])
            )
            if created:
                new_articles += 1
        logger.info("Inserted %s new articles and %s new authors", new_articles, new_authors)
