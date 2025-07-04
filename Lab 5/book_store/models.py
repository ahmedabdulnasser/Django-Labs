from django.conf import settings
from django.db import models
from django.core.exceptions import ValidationError


class Category(models.Model):
    name = models.CharField(max_length=50)

    def clean(self):
        if len(self.name) < 2:
            raise ValidationError("Category name must be at least 2 characters.")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    rate = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    views = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    categories = models.ManyToManyField(Category)

    def clean(self):
        if not (10 <= len(self.title) <= 50):
            raise ValidationError("Book title must be between 10 and 50 characters.")

    def __str__(self):
        return self.title


class ISBN(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    author_title = models.CharField(max_length=100)
    book_title = models.CharField(max_length=200)
    isbn_number = models.CharField(max_length=13, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.isbn_number:
            import uuid

            self.isbn_number = str(uuid.uuid4().int)[:13]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.isbn_number
