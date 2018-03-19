from django.db import models

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)


class Movie(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    director = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, related_name='related_name')
    year = models.IntegerField()
    actors = models.ManyToManyField(Person, through='PersonMovie')


class PersonMovie(models.Model):
    role = models.CharField(max_length=64)
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True)




