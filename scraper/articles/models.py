from django.db import models


class Author(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)

class Article(models.Model):
    text = models.TextField()
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE, default=None)



