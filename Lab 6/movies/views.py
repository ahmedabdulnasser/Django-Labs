from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie, Category, Cast, Series
from .serializers import (
    MovieSerializer,
    CategorySerializer,
    CastSerializer,
    SeriesSerializer,
)


# Movie CRUD Views (Function-Based)


@api_view(["GET", "POST"])
def movie_list_create(request):
    """
    List all movies or create a new movie.
    """
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def movie_detail(request, pk):
    """
    Retrieve, update or delete a movie.
    Supports both full update (PUT) and partial update (PATCH).
    """
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == "GET":
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    elif request.method == "PUT":
        # Full update - all fields required
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PATCH":
        # Partial update - only provided fields updated
        serializer = MovieSerializer(movie, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Category CRUD Views (Function-Based)


@api_view(["GET", "POST"])
def category_list_create(request):
    """
    List all categories or create a new category.
    """
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def category_detail(request, pk):
    """
    Retrieve, update or delete a category.
    """
    category = get_object_or_404(Category, pk=pk)

    if request.method == "GET":
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PATCH":
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Cast CRUD Views (Function-Based)


@api_view(["GET", "POST"])
def cast_list_create(request):
    """
    List all cast members or create a new cast member.
    """
    if request.method == "GET":
        casts = Cast.objects.all()
        serializer = CastSerializer(casts, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CastSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def cast_detail(request, pk):
    """
    Retrieve, update or delete a cast member.
    """
    cast = get_object_or_404(Cast, pk=pk)

    if request.method == "GET":
        serializer = CastSerializer(cast)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = CastSerializer(cast, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PATCH":
        serializer = CastSerializer(cast, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        cast.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Series CRUD Views (Function-Based)


@api_view(["GET", "POST"])
def series_list_create(request):
    """
    List all series or create a new series.
    """
    if request.method == "GET":
        series = Series.objects.all()
        serializer = SeriesSerializer(series, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = SeriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def series_detail(request, pk):
    """
    Retrieve, update or delete a series.
    """
    series = get_object_or_404(Series, pk=pk)

    if request.method == "GET":
        serializer = SeriesSerializer(series)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = SeriesSerializer(series, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PATCH":
        serializer = SeriesSerializer(series, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        series.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
