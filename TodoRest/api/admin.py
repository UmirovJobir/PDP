from django.contrib import admin

# Register your models here.
from api.models import Task

admin.site.register(Task)