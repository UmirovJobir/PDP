from django.shortcuts import render
from .models import *
from .forms import *


# Create your views here.

def home(request):
    questions = Question.objects.all()
    answers = Answer.objects.all()
    context = {"questions": questions, "answers": answers}
    return render(request, 'home.html', context)

    # if request == 'GET':
    #     form = QuesForm
    # else:
    #     form = QuesForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #
    # return render(request, 'home.html')
