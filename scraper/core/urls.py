from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from core import views

urlpatterns = [
    path('authors/', views.AuthorList.as_view()),
    path('stats/', views.show_stats, name='stats'),
    path('stats/<author>', views.show_author_stats, name='author_stats')
]

urlpatterns = format_suffix_patterns(urlpatterns)
