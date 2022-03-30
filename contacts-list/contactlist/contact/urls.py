from django.urls import path
from .views import index, addContact

urlpatterns = [
    path('', index, name='index'),
    path('add-contact/', addContact, name='add-contact'),
]