from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from todo.views import TodoViewSet

router = DefaultRouter()
router.register("todo", TodoViewSet, 'todo')

urlpatterns = [
        path('', include(router.urls)),
        path('auth/', obtain_auth_token),
]