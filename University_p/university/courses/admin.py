from django.contrib import admin

# Register your models here.

from .models import *


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    search_fields = ('name', 'code',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name',)
    list_filter = ('degree',)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    autocomplete_fields = ('specialities', 'teachers',)




