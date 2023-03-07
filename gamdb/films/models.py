from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=200)
    birth_year = models.IntegerField()

class Movie(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.TextField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)