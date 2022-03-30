from django.db import models

from films.models.actor import Actor


class Movie(models.Model):
    name = models.CharField(max_length=200)
    year = models.DateField()
    imdb = models.IntegerField(max_length=10)
    genre = models.CharField(max_length=300)
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return self.name
