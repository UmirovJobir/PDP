from django.shortcuts import render
from .forms import AnswerForm
from .models import Answer


# Create your views here.

def home(request):
    return render(request, 'home.html', )


def answer(request):
    form = AnswerForm(request.POST)
    if form.is_valid():
        form.save()
        ans = form.objects.answer
        if ans == 'YES':
            return render(request, 'page.html')
