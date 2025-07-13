from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    # Movie URLs
    path("movies/", views.movie_list_create, name="movie-list-create"),
    path("movies/<int:pk>/", views.movie_detail, name="movie-detail"),
    # Category URLs
    path("categories/", views.category_list_create, name="category-list-create"),
    path("categories/<int:pk>/", views.category_detail, name="category-detail"),
    # Cast URLs
    path("casts/", views.cast_list_create, name="cast-list-create"),
    path("casts/<int:pk>/", views.cast_detail, name="cast-detail"),
    # Series URLs
    path("series/", views.series_list_create, name="series-list-create"),
    path("series/<int:pk>/", views.series_detail, name="series-detail"),
]
