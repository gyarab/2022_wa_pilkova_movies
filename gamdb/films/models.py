from django.db import models

class Movie():
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.TextField()
