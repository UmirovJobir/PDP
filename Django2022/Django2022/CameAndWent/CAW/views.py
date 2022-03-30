from django.shortcuts import render, redirect
from .models import Came, Went
from .form import CameForm, WentForm


def came_detail(request, pk):
    came = Came.objects.get(pk=pk)

    return render(request, "CAW/came.html", {
        "came": came
    })


def home_page(request):
    return render(request, "CAW/bosh_sahifa.html")


def came_list(request):
    search = request.GET.get("search")

    if search is None:
        cames = Came.objects.all()
    else:
        cames = Came.objects.filter(first_name__contains=search)

    if request.method == 'GET':
        form = CameForm()
    else:
        form = CameForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            came = Came.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                section=data['section'],
                arrival_time=data['arrival_time'],
            )
            return redirect("came-list")

    return render(request, "CAW/cames.html", {
        "cames": cames, "search": search, "form": form,
    })


def went_list(request):
    search = request.GET.get("search")

    if search is None:
        wents = Went.objects.all()
    else:
        wents = Went.objects.filter(first_name__contains=search)

    if request.method == 'GET':
        form = WentForm()
    else:
        form = WentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            went = Went.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                section=data['section'],
                time_to_leave=data['time_to_leave'],
            )
            return redirect("went-list")

    return render(request, "CAW/wents.html", {
        "wents": wents, "search": search, "form": form,
    })
