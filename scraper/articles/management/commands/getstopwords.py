from django.core.management.base import BaseCommand, CommandError
import nltk

class Command(BaseCommand):
    help = 'Downloads nltk stopwords'

    def handle(self, *args, **options):
        nltk.download("stopwords")