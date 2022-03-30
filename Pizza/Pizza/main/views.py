from django.shortcuts import render
from .models import Pizza, Pizzas, Pizaa_About


def main(request):
    return render(request, 'main/index.html', )


def Pizzas_Views(request):
    pizza = Pizzas.objects.all()

    return render(request, 'main/pizzas.html', {
        "pizza": pizza
    })


def menu(request):
    pizza = Pizza.objects.all()

    return render(request, 'main/menu.html', {
        "pizza": pizza
    })


def about(request):
    pizza = Pizaa_About.objects.all()
    return render(request, 'main/about.html', {
        'pizzas': pizza
    })
