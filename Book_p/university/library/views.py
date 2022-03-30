from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect

from .models import Book
from .forms import BookForm


def home(request):
    return render(request, 'library/home.html',)


def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")

    return render(request, "library/book.html", {
        "book": book
    })


def books_list(request):
    search = request.GET.get("search")

    if search is None:
        books = Book.objects.all()
    else:
        books = Book.objects.filter(Q(title__icontains=search) | Q(author__icontains=search))

    return render(request, "library/books.html", {
        "books": books, "search": search,
    })


def book_create(request):
    if request == "GET":
        form = BookForm()
    else:
        form = BookForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            book = Book.objects.create(
                title=data['title'],
                author=data['author'],
                count=data['count'],
            )
            return redirect("books-list")

    return render(request, "library/book_create.html", {
        "form": form,
    })
