from django.apps import AppConfig
import nltk


class ArticlesConfig(AppConfig):
    name = 'articles'

    def ready(self):
        nltk.download("stopwords")
