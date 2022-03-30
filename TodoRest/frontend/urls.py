from django.urls import path

from frontend.views import list

urlpatterns = [
    path('', list, name='list'),
]