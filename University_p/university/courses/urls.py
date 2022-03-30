from django.urls import path
from .views import *

urlpatterns = [
    path("courses/speciality/", Speciality_list, name='Speciality_list'),
    path("courses/teacher/", Teacher_list, name='Teacher_list'),
    path("courses/subject/", Subject_list, name='Subject_list'),
    path("courses/subject/<int:pk>/", Subject_detail, name='Subject_detail'),
    path("courses/speciality/create/", Speciality_create, name='Speciality_create'),
    path("courses/teacher/create/", Teacher_create, name='Teacher_create'),
    path("courses/subject/create/", Subject_create, name='Subject_create'),
]