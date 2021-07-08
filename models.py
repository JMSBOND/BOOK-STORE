from django.db import models


class Book (models.Model):
    bookname = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    language = models.CharField(max_length=100)

# Create your models here.
