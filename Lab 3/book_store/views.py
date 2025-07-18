from django.shortcuts import HttpResponse, render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm


def index(request):
    return HttpResponse("Hello world")


def book_list(request):
    books = Book.objects.all()
    return render(request, "book_list.html", {"books": books})


def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "book_form.html", {"form": form})


def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "book_form.html", {"form": form})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "book_confirm_delete.html", {"book": book})
