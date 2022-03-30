
from django.shortcuts import render

from .models import Book


def books_view(request):
    books = Book.objects.all()
    return render(request, "library/books.html", {
        "books": books,
    })


