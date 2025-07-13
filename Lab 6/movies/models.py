from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Cast(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=100, blank=True, null=True)
    profile_image = models.ImageField(upload_to="cast_images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class BaseContent(models.Model):
    """Abstract base class for Movie and Series"""

    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    categories = models.ManyToManyField(Category, related_name="%(class)s_set")
    casts = models.ManyToManyField(Cast, related_name="%(class)s_set")
    poster_image = models.ImageField(upload_to="posters/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Movie(BaseContent):
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    budget = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    box_office = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True
    )

    class Meta:
        ordering = ["-release_date"]

    def __str__(self):
        return f"{self.title} ({self.release_date.year})"


class Series(BaseContent):
    seasons = models.PositiveIntegerField(default=1)
    episodes = models.PositiveIntegerField(default=1)
    status = models.CharField(
        max_length=20,
        choices=[
            ("ongoing", "Ongoing"),
            ("completed", "Completed"),
            ("cancelled", "Cancelled"),
        ],
        default="ongoing",
    )
    average_episode_duration = models.PositiveIntegerField(
        help_text="Average episode duration in minutes", blank=True, null=True
    )

    class Meta:
        ordering = ["-release_date"]
        verbose_name_plural = "Series"

    def __str__(self):
        return f"{self.title} ({self.release_date.year}) - {self.seasons} Season(s)"
