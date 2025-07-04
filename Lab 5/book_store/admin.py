from django.contrib import admin
from .models import Book, Category, ISBN

class ISBNInline(admin.StackedInline):
    model = ISBN
    can_delete = False

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'rate', 'views')
    list_filter = ('user', 'categories')
    inlines = [ISBNInline]  # Add this line

admin.site.register(Book, BookAdmin)
admin.site.register(Category)
admin.site.register(ISBN)
