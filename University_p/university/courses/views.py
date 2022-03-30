from django.db.models import Q
from django.shortcuts import render, redirect

from .models import *
from .forms import SpecialityForm, TeacherForm, SubjectForm


def Speciality_list(request):
    specialities = Speciality.objects.all()

    return render(request, "speciality_list.html", {
        "specialities": specialities
    })


def Teacher_list(request):
    search = request.GET.get('search', "")

    if search:
        teachers = Teacher.objects.filter(Q(first_name__icontains=search) | Q(last_name__icontains=search))
    else:
        teachers = Teacher.objects.all()

    return render(request, "teacher_list.html", {
        "teachers": teachers, "search": search
    })


def Subject_list(request):
    subjects = Subject.objects.all()

    return render(request, "subjects_list.html", {
        "subjects": subjects
    })


def Subject_detail(request, pk):
    subject = Subject.objects.get(pk=pk)
    teachers = subject.teachers.all()
    specialities = subject.specialities.all()

    return render(request, "subject.html", {
        "subject": subject, "teachers": teachers, "specialities": specialities
    })


def Speciality_create(request):
    if request == "GET":
        form = SpecialityForm()
    else:
        form = SpecialityForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            speciality = Speciality.objects.create(
                name=data['name'],
                code=data['code'],
                start_date=data['start_date'],
                is_active=data['is_active'],
            )
            return redirect("Speciality_list")

    return render(request, "speciality_create.html", {
        "form": form,
    })


def Teacher_create(request):
    if request == "GET":
        form = TeacherForm()
    else:
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Teacher_list")

    return render(request, "teacher_create.html", {
        "form": form
    })


def Subject_create(request):
    if request == "GET":
        form = SubjectForm()
    else:
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Subject_list")

    return render(request, "subject_create.html", {
        "form": form
    })
