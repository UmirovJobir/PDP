from django.urls import path

from api.views import apiOverview, tasklist, taskDetail, taskCreate, taskUpdate, taskDelete

urlpatterns = [
    path('', apiOverview, name='api-overview'),
    path('task-list/', tasklist, name='task-list'),
    path('task-detail/<str:pk>/', taskDetail, name='task-detail'),
    path('task-create/', taskCreate, name='task-create'),
    path('task-update/<str:pk>/', taskUpdate, name='task-update'),
    path('task-delete/<str:pk>/', taskDelete, name='task-delete'),
]
