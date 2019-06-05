from django.urls import path

from .views import kick_scooter_page

urlpatterns = [
    path('', kick_scooter_page),
]