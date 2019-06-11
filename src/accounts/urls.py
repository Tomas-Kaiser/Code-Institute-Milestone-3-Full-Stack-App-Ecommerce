from django.urls import path
from .views import (
   indexView,
   dashboardView,
)

urlpatterns = [
    path('', indexView, name="home"),
    path('dasboard/', dashboardView, name="dashboard"),
    path('login/',),
    path('register/',),
    path('logout/',),
]
