from django.contrib import admin
from .models import *


# Register your models here.
class AnswerInline(admin.TabularInline):
    model = Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline,
    ]


admin.site.register(Answer)
# admin.register(Question, QuestionAdmin)
