from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from articles.models import Article, Author
from articles.modules.word_counter import get_stats
from articles.serializers import ArticleSerializer


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class AuthorList(APIView):
    def get(self, request):
        """
        Return a list of all users.
        """
        usernames = {author.id: author.name for author in Author.objects.all()}
        return Response(usernames)

@api_view(["GET"])
def show_stats(request):
    articles = Article.objects.all()

    return Response(get_stats(articles))


@api_view(["GET"])
def show_author_stats(request, author):
    articles = Article.objects.filter(author_id=author)

    return Response(get_stats(articles))
