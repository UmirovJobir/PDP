from django import forms
from django.forms import ModelForm
from .models import Answer


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'


