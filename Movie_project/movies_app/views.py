from django.shortcuts import render , get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from movies_app.serializers import MovieSerializer, PersonSerializer
from movies_app.models import Movie, Person


# Create your views here.

class MoviesView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True, context={'request': request})   # many przy wielu obiektaach
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieView(APIView):
    def get(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def delete(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonsView(APIView):
    def get(self, request):
        persons= Person.objects.all()
        serializer = PersonSerializer(persons, many=True, context={'request': request})   # many przy wielu obiektaach
        return Response(serializer.data)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonView(APIView):
    def get(self, request, pk):
        person = get_object_or_404(Person, pk=pk)
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    def delete(self, request, pk):
        person = get_object_or_404(Person, pk=pk)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        person = get_object_or_404(Movie, pk=pk)
        serializer = PersonSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
