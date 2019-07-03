from django.urls import path, include

from .views import (
   register_page,
   profile,
)

urlpatterns = [
   path('', include('django.contrib.auth.urls')),
   path('register/', register_page, name="register"),
   path('profile/', profile, name="profile"),
]
