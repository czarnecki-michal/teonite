from rest_framework import generics
from articles.models import Article
from articles.models import Author
from articles.serializers import ArticleSerializer
from articles.word_counter import compute_stats
from rest_framework.decorators import api_view
from rest_framework.response import Response
import operator
import collections
from rest_framework.views import APIView


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class AuthorList(APIView):
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = {author.id: author.name for author in Author.objects.all()}
        return Response(usernames)

@api_view(["GET"])
def show_stats(request):
    articles = Article.objects.all()

    words = {}

    for article in articles:
        article_stats = compute_stats(article.text)

        for word in article_stats:
            if word not in words:
                words[word] = article_stats[word]
            elif word in words:
                words[word] += article_stats[word]
    data = sorted(words.items(), key=operator.itemgetter(1), reverse=True)[:10]
    sorted_dict = collections.OrderedDict(data)
    return Response(sorted_dict)


@api_view(["GET"])
def show_author_stats(request, author):
    articles = Article.objects.filter(author_id=author)

    words = {}

    for article in articles:
        article_stats = compute_stats(article.text)

        for word in article_stats:
            if word not in words:
                words[word] = article_stats[word]
            elif word in words:
                words[word] += article_stats[word]
    data = sorted(words.items(), key=operator.itemgetter(1), reverse=True)[:10]
    sorted_dict = collections.OrderedDict(data)
    return Response(sorted_dict)