from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import date
from .models import Movie, Review
from datetime import datetime

def home(request):
    upcoming_movies = Movie.objects.filter(release_date__gte = datetime.date(datetime.now()))
    current_movies = Movie.objects.filter(release_date__lt = datetime.date(datetime.now()))
    context = {
        "next_url": "/",
        "page_url": "home",
        "upcoming_movies": upcoming_movies,
        "current_movies": current_movies.order_by('-rating', 'name')
    }
    return render(request, "index.html", context)

def feed(request):
    return HttpResponse("<h1>Feed</h1>")

def search(request):
    context = {
        "next_url": "/search/",
        "page_url": "browse",
        "movie_genres": list(Movie.objects.values_list('genre', flat=True).distinct().order_by('genre')),
        "movie_languages": list(
                   Movie.objects.values_list('language', flat=True).distinct().order_by('language'))
    }
    if request.method == "GET":
        context["searched_movies"] = Movie.objects.all().order_by('name')
        context["search_form"] = {}
        return render(request, "search.html", context)

    elif request.method == "POST":

        movies_names = movies_genres = movies_year_start = movies_year_end = movies_language = movies_rating = Movie.objects.all()

        if request.POST.get("name", False) and request.POST["name"]:
            movies_names = Movie.objects.filter(name__icontains = request.POST["name"])

        if request.POST.get("genre", False) and request.POST["genre"] and request.POST["genre"] != 'any':
            movies_genres = Movie.objects.filter(genre = request.POST["genre"])

        if request.POST.get("date_start", False) and request.POST["date_start"]:
            movies_year_start = Movie.objects.filter(release_date__gte = request.POST["date_start"])
        
        if request.POST.get("date_end", False) and request.POST["date_end"]:
            movies_year_end = Movie.objects.filter(release_date__lte = request.POST["date_end"])

        if request.POST.get("language", False) and request.POST["language"] and request.POST["language"] != 'any':
            movies_language = Movie.objects.filter(language = request.POST["language"])

        if request.POST.get("rating", False) and request.POST["rating"] and request.POST["rating"] != '0':
            movies_rating = Movie.objects.filter(rating__gte = float(request.POST["rating"]))

        searched_movies = movies_names & movies_genres & movies_year_start & movies_year_end & movies_language & movies_rating

        context["searched_movies"] = searched_movies.order_by('name')
        context["search_form"] = request.POST

        return render(request, "search.html", context)

def movie(request, id):
    movie_object = Movie.objects.filter(id=id)[0]
    reviews = Review.objects.filter(movie=movie_object)
    review_count = len(reviews)
    # is_released?
    users_count = [0]*5
    users_percent = [0]*5
    for i in reviews:
        users_count[i.rating - 1] += 1
    if reviews:
        for i in range(5):
            users_percent[i - 1] = (users_count[i - 1]//review_count) * 100
    context = {
        "movie": movie_object,
        "movie_released": movie_object.release_date < date.today(),
        "reviews": reviews,
        "users_count": users_count,
        "users_percent": users_percent
    }
    return render(request, "movie.html", context)

def add_review(request):
    if request.method == "POST":
        params = request.POST
        rating = int(params.get('rating_val', [0])[0])
        title = params.get('review_title', 'None')
        text = params.get('review_text', 'None')
        movie_id = int(params.get('movie_id', ['0'])[0])
        movie_object = Movie.objects.filter(id=movie_id)[0]
        reviews = Review.objects.filter(movie=movie_object)
        review_count = len(reviews)
        new_rating = (review_count*movie_object.rating + rating)/(review_count+1)
        if len(str(new_rating))>3:
            new_rating = float(str(new_rating)[:3])
        old_obj, new_obj = Movie.objects.update_or_create(
            id=movie_id,
            defaults={'rating': new_rating}
        )
        new_review = Review(
            title=title,
            text=text,
            date=date.today(),
            rating=rating,
            movie=Movie.objects.filter(id=movie_id)[0],
            user=request.user
        )
        new_review.save()
        return redirect(params.get('next'))

def get_all_reviews(request):
    if not request.user:
        return redirect(request.GET.get("next", "/"))
    rating_counts, ratings_percent = [0]*5, [0]*5
    list_of_reviews = Review.objects.filter(user=request.user)
    average_rating, count = 0, len(list_of_reviews)
    for i in list_of_reviews:
        average_rating += i.rating
        rating_counts[i.rating - 1] += 1
    for i in range(5):
        ratings_percent = (rating_counts[i]/count)*100
    average_rating = (average_rating/count) if count else 0
    if len(str(average_rating))>3:
        average_rating = float(str(average_rating)[:3])
    context = {
        "average_rating": average_rating,
        "rating_counts": rating_counts,
        "ratings_percent": ratings_percent,
        "reviews": list_of_reviews
    }
    return render(request, 'reviews.html', context)

def login_request(request):
    if request.method == 'GET':
        form = AuthenticationForm(request=request, data=request.GET)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
        return redirect(request.GET.get("next", "/"))

def logout_request(request):
    logout(request)
    return redirect(request.GET.get("next", "/"))
