import uuid
from django.db import models

from .utils import make_uuid

# Create your models here.
class Person(models.Model):
    uuid = models.UUIDField(default=make_uuid)
    first_name = models.CharField(max_length=268)
    last_name = models.CharField(max_length=268, blank=True, null=True)
    birthdate = models.DateTimeField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)


    @property
    def names(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Country(models.Model):
    uuid = models.UUIDField(default=make_uuid)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Genre(models.Model):
    uuid = models.UUIDField(default=make_uuid)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Movie(models.Model):
    uuid = models.UUIDField(default=make_uuid)
    name_rus = models.CharField(max_length=256)
    name_orig = models.CharField(max_length=256)
    year = models.PositiveIntegerField()
    image = models.URLField()
    rating = models.DecimalField(blank=True, null=True, decimal_places=1, max_digits=3)
    country = models.ManyToManyField(to=Country)
    actors = models.ManyToManyField(to=Person, related_name='actors')
    director = models.ManyToManyField(to=Person, related_name='director')
    genre = models.ManyToManyField(to=Genre)

    def serialize(self):
        return {
            'id': self.uuid,
            'movieTitleOrig': self.name_orig,
            'movieTitleRus': self.name_rus,
            'country': self.country.all(),
            'movieActors': self.actors.all(),
            'director': self.director,
            'movieRate': self.rating,
            'year': self.year,
            'genre': self.genre.all(),
            'movieImageUrl': self.image,
        }