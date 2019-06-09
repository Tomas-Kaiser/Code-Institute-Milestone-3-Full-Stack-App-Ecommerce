from django.urls import path

from .views import (
    kick_scooter_page,
    kick_scooter_detail,
)

urlpatterns = [
    path('', kick_scooter_page, name="kick-scooter"),
    path('<str:slug>', kick_scooter_detail),
]