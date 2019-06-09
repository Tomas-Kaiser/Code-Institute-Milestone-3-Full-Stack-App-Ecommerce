from django.urls import path

from .views import (
    kick_scooter_page,
    kick_scooter_detail,
    eScooter_page,
    kid_scooter_page,
)

urlpatterns = [
    path('kick-scooters/', kick_scooter_page, name="kick-scooter-products"),
    path('eScooters/', eScooter_page, name="eScooter-products"),
    path('kid-scooters/', kid_scooter_page, name="kid-scooter-products"),
    path('kick-scooters/<str:slug>', kick_scooter_detail),   
]