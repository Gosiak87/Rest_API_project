from .models import Movie, Person
from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("title", "description", "director", "year", "actors")


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ("role", "person", "movie")
