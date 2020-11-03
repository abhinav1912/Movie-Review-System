from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie
from datetime import datetime

def home(request):
    movies = Movie.objects.all()
    upcoming_movies = []
    current_movies = []
    for movie in movies:
        if movie.release_date <= datetime.date(datetime.now()):
            current_movies.append(movie)
        else:
            upcoming_movies.append(movie)
    
    context = {}
    context["page_title"] = "Home"
    context["upcoming_movies"] = upcoming_movies
    context["current_movies"] = current_movies

    return render(request, "index.html", context)

def feed(request):
    return HttpResponse("<h1>Feed</h1>")

def search(request):
    if request.method == "GET":
        context = {}
        context["searched_movies"] = []
        return render(request, "search.html", context)

    elif request.method == "POST":
        print(request.POST)

        movies_names = movies_genres = movies_year = movies_language = movies_rating = Movie.objects.all()

        if(request.POST["name"]!=''):
            movies_names = Movie.objects.filter(name__icontains = request.POST["name"])

        if(request.POST["genre"]!='any'):
            movies_genres = Movie.objects.filter(genre = request.POST["genre"])

        if(request.POST["date_start"]!='1900-01-01' and request.POST["date_end"]!='2200-01-01'):
            movies_year = Movie.objects.filter(release_date__range = [request.POST["date_start"], request.POST["date_end"]])

        if(request.POST["language"]!='any'):
            movies_language = Movie.objects.filter(language = request.POST["language"])

        if(request.POST["rating"]!='0'):
            movies_rating = Movie.objects.filter(rating__gte = float(request.POST["rating"]))

        searched_movies = movies_names & movies_genres & movies_year & movies_language & movies_rating

        # for movie in searched_movies:
        #     print(movie.name)
        
        context = {}
        context["searched_movies"] = searched_movies

        return render(request, "search.html", context)

def movie(request, id):
    return HttpResponse("<h1>Movie Page</h1>")