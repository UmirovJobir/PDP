from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home-list'),
    path('books/', books_list, name='books-list'),
    path('books/<int:pk>/', book_detail, name='book-detail'),
    path('books/create/', book_create, name='book-create'),
]
