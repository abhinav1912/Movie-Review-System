from django.contrib.auth.models import User
from djongo import models

class Movie(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    release_date = models.DateField()

class Review(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    text = models.CharField(max_length=150)
    rating = models.IntegerField()
    movie = models.EmbeddedField(model_container=Movie, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
