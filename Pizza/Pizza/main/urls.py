from django.urls import path
from .views import main, Pizzas_Views, menu, about
urlpatterns = [
    path('', main, name="main-p"),
    path('pizzas/', Pizzas_Views, name='pizzas'),
    path('menu/', menu, name='menu'),
    path('about/', about, name='about'),
]
