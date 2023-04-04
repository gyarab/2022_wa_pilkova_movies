from django.shortcuts import render
from .models import Movie, Director


def homepage(request):
    context = {
        "movies": Movie.objects.all()
    }
  
    return render(request, 'main.html', context)

def directors(request):
    context = {
        "logic": True,
        "title": "Nejoblíbenější herci",
        "directors": Director.objects.all()
    }
  
    return render(request, 'directors.html', context)



# Create your views here.