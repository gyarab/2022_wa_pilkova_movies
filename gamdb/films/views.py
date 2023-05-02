from django.shortcuts import render
from .models import Movie, Director, Actor, Genre, Comment
from django.db.models import Q

def directors(request):
    context = {
        'directors': Director.objects.all()
    }
    print(context)
    return render(request, 'directors.html', context)

def director(request, id):
    context = {
        "director": Director.objects.get(id=id)
    }
    return render(request, 'director.html', context)

def movies(request):
    movie_queryset = Movie.objects.all()
    genres = request.GET.get('genre')
    if genres:
        movie_queryset = movie_queryset.filter(genre__name=genres)
    search = request.GET.get('search')
    if search:
        movie_queryset = movie_queryset.filter(Q(name__icontains=search)|Q(description__icontains=search))
    context = {
        "movies": movie_queryset,
        "genres": Genre.objects.all().order_by,
        "genre": genres,
        "search": search
    }
    
    return render(request, 'movies.html', context)

def movie(request, id):
    m =  Movie.objects.get(id=id)
    context = {
        "movie": m,
        "coments": Comment.objects.filter(movie=m)
    }
    return render(request, 'movie.html', context)

def actors(request):
    context = {
        "actors": Actor.objects.all()
    }
    return render(request, 'actors.html', context)

def actor(request, id):
    context = {
        "actor": Actor.objects.get(id=id)
    }
    return render(request, 'actor.html', context)

def homepage(request):
    context = {
        # TODO use first 10 top rated
        "movies": Movie.objects.all(),
        "actors": Actor.objects.all(),
        "directors": Director.objects.all(),
        "genres": Genre.objects.all(),
    }
    return render(request, 'homepage.html', context)