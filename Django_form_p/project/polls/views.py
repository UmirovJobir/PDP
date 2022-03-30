from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .form import CustomorForm
from .models import Customer


def index(request):
    if request == 'GET':
        form = CustomorForm()
    else:
        form = CustomorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            customor = Customer.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
            )
            return redirect('index')

    context = {'form': form}
    return render(request, 'index.html', context)
