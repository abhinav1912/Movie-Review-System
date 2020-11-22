from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movie/<int:id>', views.movie, name="movie"),
    path('feed/', views.feed, name='feed'),
    path('search/', views.search, name='search'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout'),
    path('movie/review/', views.add_review, name='review'),
    path('reviews/', views.get_all_reviews, name='get_all_reviews'),
    path('favourites/', views.all_favourites, name='all_favourites'),
    path('favourites/add/', views.add_favourites, name='add_favourites'),
    path('favourites/delete/', views.delete_favourites, name='del_favourites')
]