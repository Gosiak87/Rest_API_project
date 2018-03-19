from django.contrib import admin
from movies_app.models import Person, Movie, PersonMovie

# Register your models here.

admin.site.register(Person)
admin.site.register(Movie)
admin.site.register(PersonMovie)