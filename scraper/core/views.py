from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Article, Author
from core.modules.word_counter import get_stats
from core.serializers import ArticleSerializer


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
