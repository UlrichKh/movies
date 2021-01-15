from django.db.models import fields
from rest_framework import serializers
from movies.models import Movie, Person

class MovieAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'uuid',
            'name_rus',
            'name_orig',
            'year',
            'image',
            'rating',
            'country',
            'genre',
        )

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"

class MovieSerializer(serializers.ModelSerializer):
    actors = PersonSerializer(
        many=True,
        read_only=False,
    )

    director = PersonSerializer(
        many=True,
        read_only=False,
    )

    class Meta:
        model = Movie
        fields = (
            'uuid',
            'name_rus',
            'name_orig',
            'year',
            'image',
            'rating',
            'country',
            'actors',
            'director',
            'genre',
        )

