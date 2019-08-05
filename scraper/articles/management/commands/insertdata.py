from django.core.management.base import BaseCommand, CommandError
from articles.models import Author, Article
from articles.modules.scraper import Scraper
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class Command(BaseCommand):
    help = 'Inserts scraped data from blog into database'

    def handle(self, *args, **options):
        scraper = Scraper("https://teonite.com/blog/")
        posts = scraper.get_posts()

        logger.info(f"Updating {len(posts)} articles.")
        new_articles = 0
        new_authors = 0
        for post, author in posts:
            obj, created = Author.objects.update_or_create(
                id=author[0],
                name=author[1]
            )
            if created:
                new_articles += 1
            obj, created = Article.objects.update_or_create(
                text=post,
                author_id=Author.objects.get(id=author[0])
            )
            if created:
                new_authors += 1
        
        logger.info(f"Inserted {new_articles} new articles and {new_authors} new authors")
