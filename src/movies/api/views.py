from rest_framework import generics

from movies.api.serializers import MovieSerializer, MovieAllSerializer
from movies.models import Movie

class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieAllSerializer


class MovieCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    