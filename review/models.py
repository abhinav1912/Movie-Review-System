from django.contrib.auth.models import User
from djongo import models

class Movie(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    synposis = models.TextField()
    rating = models.FloatField()
    release_date = models.DateField()
    poster_link = models.TextField()
    trailer_link = models.TextField()

class Review(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    text = models.CharField(max_length=150)
    rating = models.IntegerField()
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
