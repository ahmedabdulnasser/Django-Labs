from django.core.management.base import BaseCommand
from book_store.models import Category


class Command(BaseCommand):
    help = "Create initial categories for books."

    def handle(self, *args, **options):
        categories = [
            "Fiction",
            "Non-Fiction",
            "Science",
            "History",
            "Biography",
            "Children",
        ]
        for name in categories:
            obj, created = Category.objects.get_or_create(name=name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Category "{name}" created.'))
            else:
                self.stdout.write(f'Category "{name}" already exists.')
