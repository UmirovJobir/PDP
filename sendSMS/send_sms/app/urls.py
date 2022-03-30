from django.urls import path

from .views import send, check_date

urlpatterns = [
    path('sms/', check_date, name="check-date"),
]