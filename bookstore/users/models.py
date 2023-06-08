from django.db import models

# Create your models here.

class Address(models.Model):
    street = models.CharField(max_length=100)
    number = models.IntegerField()
    city = models.CharField(max_length=100)


class User(models.Model):
    name = models.CharField(max_length=100)
    address = models.ManyToManyField(Address)
    is_member = models.BooleanField(default=False)


class LibAdmin(models.Model):
    user = models.OneToOneField(User)
    role = models.CharField(max_length=100)