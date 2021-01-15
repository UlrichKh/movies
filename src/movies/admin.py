from django.contrib import admin

from .models import Country, Genre, Movie, Person

# Register your models here.
admin.site.register(Movie)
admin.site.register(Person)
admin.site.register(Genre)
admin.site.register(Country)