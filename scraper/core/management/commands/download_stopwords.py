from django.core.management.base import BaseCommand
import nltk


class Command(BaseCommand):
    help = 'Inserts scraped data from blog into database'
    def handle(self, *args, **options):
        nltk.download("stopwords")
