from django.db import models

# Create your models here.
from ..users.models import *


class Genre(models.Model):
    title = models.CharField(max_length=100)

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.ManyToManyField(Address)

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    genre = models.ManyToManyField(Genre)
    author = models.ManyToManyField(Author)
    publisher = models.ManyToManyField(Publisher)
    quantity = models.IntegerField()


class Borrowed(models.Model):
    user = models.ManyToManyField(User)
    book = models.ManyToManyField(Book) # TODO change this relation
    time = models.DateTimeField()
    # status = models.BooleanField() # TODO change to enumerate