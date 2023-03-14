from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=200)
    
    birth_year = models.IntegerField()
    def _str_(self):
        return f"{self.name} ({self.birth_year})"

class Movie(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.TextField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def _str_(self):
       return f"{self.name} ({self.year}) {self.director}"