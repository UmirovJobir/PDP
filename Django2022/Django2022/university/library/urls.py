from django.urls import path
from .views import books_view

urlpatterns = [
    path("books/",  books_view, name="books")
]