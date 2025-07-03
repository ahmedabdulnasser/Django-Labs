from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    rate = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)  # Added default
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
