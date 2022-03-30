from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Movie, Actor
from .serializer import ActorSerializer, MovieSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
