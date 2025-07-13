from rest_framework import serializers
from .models import Category, Cast, Movie, Series


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]


class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = [
            "id",
            "name",
            "bio",
            "birth_date",
            "nationality",
            "profile_image",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]


class MovieSerializer(serializers.ModelSerializer):
    # For display purposes (bonus requirement)
    categories_display = CategorySerializer(
        source="categories", many=True, read_only=True
    )
    casts_display = CastSerializer(source="casts", many=True, read_only=True)

    # For write operations
    categories = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), many=True, write_only=True
    )
    casts = serializers.PrimaryKeyRelatedField(
        queryset=Cast.objects.all(), many=True, write_only=True
    )

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "description",
            "release_date",
            "duration",
            "rating",
            "budget",
            "box_office",
            "poster_image",
            "categories",
            "casts",
            "categories_display",
            "casts_display",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]

    def to_representation(self, instance):
        """Override to include categories and casts with their string representation"""
        data = super().to_representation(instance)

        # Remove write-only fields from response
        data.pop("categories", None)
        data.pop("casts", None)

        # Rename display fields to original names
        data["categories"] = data.pop("categories_display", [])
        data["casts"] = data.pop("casts_display", [])

        return data


class SeriesSerializer(serializers.ModelSerializer):
    # For display purposes
    categories_display = CategorySerializer(
        source="categories", many=True, read_only=True
    )
    casts_display = CastSerializer(source="casts", many=True, read_only=True)

    # For write operations
    categories = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), many=True, write_only=True
    )
    casts = serializers.PrimaryKeyRelatedField(
        queryset=Cast.objects.all(), many=True, write_only=True
    )

    class Meta:
        model = Series
        fields = [
            "id",
            "title",
            "description",
            "release_date",
            "seasons",
            "episodes",
            "status",
            "average_episode_duration",
            "poster_image",
            "categories",
            "casts",
            "categories_display",
            "casts_display",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]

    def to_representation(self, instance):
        """Override to include categories and casts with their string representation"""
        data = super().to_representation(instance)

        # Remove write-only fields from response
        data.pop("categories", None)
        data.pop("casts", None)

        # Rename display fields to original names
        data["categories"] = data.pop("categories_display", [])
        data["casts"] = data.pop("casts_display", [])

        return data
