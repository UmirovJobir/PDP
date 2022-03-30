from django.urls import path
from .views import came_list, came_detail, went_list, home_page

urlpatterns = [
    path("cames/", came_list, name="came-list"),
    path("cames/<int:pk>/", came_detail, name="came-detail"),
    path("wents/", went_list, name="went-list"),
    path("", home_page, name="home_page")

]