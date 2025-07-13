from django.contrib import admin
from .models import Category, Cast, Movie, Series


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at"]
    search_fields = ["name"]
    ordering = ["name"]


@admin.register(Cast)
class CastAdmin(admin.ModelAdmin):
    list_display = ["name", "nationality", "birth_date", "created_at"]
    search_fields = ["name", "nationality"]
    list_filter = ["nationality", "birth_date"]
    ordering = ["name"]


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["title", "release_date", "duration", "rating", "created_at"]
    search_fields = ["title", "description"]
    list_filter = ["release_date", "rating", "categories"]
    filter_horizontal = ["categories", "casts"]
    ordering = ["-release_date"]


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "release_date",
        "seasons",
        "episodes",
        "status",
        "created_at",
    ]
    search_fields = ["title", "description"]
    list_filter = ["release_date", "status", "seasons", "categories"]
    filter_horizontal = ["categories", "casts"]
    ordering = ["-release_date"]
