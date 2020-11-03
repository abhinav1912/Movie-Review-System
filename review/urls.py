from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movie/<int:id>', views.movie, name="movie"),
    path('feed/', views.feed, name='feed'),
    path('search/', views.search, name='search'),
]