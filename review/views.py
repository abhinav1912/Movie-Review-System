from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie
from datetime import datetime

def home(request):
    upcoming_movies = Movie.objects.filter(release_date__gte = datetime.date(datetime.now()))
    current_movies = Movie.objects.filter(release_date__lt = datetime.date(datetime.now()))
    context = {}
    context["page_url"] = "home"
    context["upcoming_movies"] = upcoming_movies
    context["current_movies"] = current_movies.order_by('-rating', 'name')
    return render(request, "index.html", context)

def feed(request):
    return HttpResponse("<h1>Feed</h1>")

def search(request):
    context = {}
    context["page_url"] = "browse"
    context["movie_genres"] = list(Movie.objects.values_list('genre', flat=True).distinct().order_by('genre'))
    context["movie_languages"] = list(Movie.objects.values_list('language', flat=True).distinct().order_by('language'))
    if request.method == "GET":
        context["searched_movies"] = Movie.objects.all().order_by('name')
        context["search_form"] = {}
        return render(request, "search.html", context)

    elif request.method == "POST":

        movies_names = movies_genres = movies_year_start = movies_year_end = movies_language = movies_rating = Movie.objects.all()

        if(request.POST["name"]!=''):
            movies_names = Movie.objects.filter(name__icontains = request.POST["name"])

        if(request.POST["genre"]!='any'):
            movies_genres = Movie.objects.filter(genre = request.POST["genre"])

        if(request.POST["date_start"]!=''):
            movies_year_start = Movie.objects.filter(release_date__gte = request.POST["date_start"])
        
        if(request.POST["date_end"]!=''):
            movies_year_end = Movie.objects.filter(release_date__lte = request.POST["date_end"])

        if(request.POST["language"]!='any'):
            movies_language = Movie.objects.filter(language = request.POST["language"])

        if(request.POST["rating"]!='0'):
            movies_rating = Movie.objects.filter(rating__gte = float(request.POST["rating"]))

        searched_movies = movies_names & movies_genres & movies_year_start & movies_year_end & movies_language & movies_rating

        context["searched_movies"] = searched_movies.order_by('name')
        context["search_form"] = request.POST

        return render(request, "search.html", context)

def movie(request, id):
    return HttpResponse("<h1>Movie Page</h1>")