from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActorViewSet, ModelViewSet


router = DefaultRouter()
router.register('movies', ModelViewSet, basename='ModelView')
router.register('actors', ActorViewSet, basename='ActorView')

urlpatterns = [
    path('', include(router.urls)),
]