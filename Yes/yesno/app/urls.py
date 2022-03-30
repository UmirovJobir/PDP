from django.urls import path
from .views import home

Urlpatterns = [
    path('', home, name='home')
]
