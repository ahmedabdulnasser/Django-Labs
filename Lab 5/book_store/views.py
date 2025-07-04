from django.shortcuts import HttpResponse, render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            form = UserCreationForm()
    return render(request, "registration/signup.html")


@login_required
def index(request):
    return HttpResponse("Hello world")


@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, "book_list.html", {"books": books})


@login_required
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            form.save_m2m()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "book_form.html", {"form": form})


@login_required
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if book.user != request.user:
        return HttpResponse("Unauthorized", status=403)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "book_form.html", {"form": form})


@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if book.user != request.user:
        return HttpResponse("Unauthorized", status=403)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "book_confirm_delete.html", {"book": book})
