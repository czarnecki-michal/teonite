from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from articles import views

urlpatterns = [
    path('articles/', views.ArticleList.as_view()),
    path('articles/<int:pk>/', views.ArticleDetail.as_view()),
    path('authors/', views.AuthorList.as_view()),
    path('stats/', views.show_stats, name='stats'),
    path('stats/<author>', views.show_author_stats, name='author_stats')
]

urlpatterns = format_suffix_patterns(urlpatterns)
