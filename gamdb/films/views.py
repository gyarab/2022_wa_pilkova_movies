from django.shortcuts import render
from .models import Movie, Director


def homepage(request):
    context = {
        "movies": Movie.objects.all()
    }
  
    return render(request, 'homepage.html', context)

def movies(request):
    context = {
        "movies": Movie.objects.all()
    }
  
    return render(request, 'movies.html', context)
    
def detaily(request):
    context = {
        "movies": Movie.objects.all()
    }
  
    return render(request, 'detaily.html', context)

def directors(request):
    context = {
        "logic": True,
        "title": "Nejoblíbenější herci",
        "directors": Director.objects.all()
    }
  
    return render(request, 'directors.html', context)



# Create your views here.