from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "countries"


class Actor(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    born_year = models.IntegerField()
    
    class Meta:
        db_table = "actors"


class Director(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    born_year = models.IntegerField()
    class Meta:
        db_table = "directors"


class Genre(models.Model):
    title = models.CharField(max_length=255)
    class Meta:
        db_table = "genres"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    year = models.IntegerField()
    rating = models.IntegerField()
    actors = models.ManyToManyField(Actor)
    genres = models.ManyToManyField(Genre)
    directors = models.ManyToManyField(Director)
    
    class Meta:
        db_table = "movies"


class Sale(models.Model):                         
    amount = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
    class Meta:
        db_table = "sales"
