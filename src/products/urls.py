from django.urls import path

from .views import (
    kick_scooter_page,
    kick_scooter_detail,
)

urlpatterns = [
    path('kick-scooters/', kick_scooter_page, name="kick-scooter"),
    path('kick-scooters/<str:slug>', kick_scooter_detail),
]