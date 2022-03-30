from django import forms
from datetime import datetime


class CameForm(forms.Form):
    first_name = forms.CharField(max_length=200, label="Xodimning ismi")
    last_name = forms.CharField(max_length=200, label="Xodimning familasi")
    section = forms.ChoiceField(label="Bo'limingizni tanlang", choices=[('ishlab chiqarish', 'Ishlab chiqarish'),
                                                                        ("qurilish bo'limi", "Qurilish bo'limi"),
                                                                        ("mexanika bo'limi", "Mexanika bo'limi"),
                                                                        ("iqtisod bo'limi", "Iqtisod bo'limi"),
                                                                        ("Ijro bo'limi", "Ijro bo'limi"),
                                                                        ("energetika bo'limi", "Energetika bo'limi")])
    arrival_time = forms.DateField(label="Kelgan vaqtingiz", )


class WentForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    section = forms.CharField(max_length=200)
    time_to_leave = forms.DateTimeField()
