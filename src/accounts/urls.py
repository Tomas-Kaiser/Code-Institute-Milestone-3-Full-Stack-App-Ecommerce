from django.urls import path
from .views import (
   register_page,
   login_page,
   logout,
   profile,
)

urlpatterns = [
   path('register/', register_page, name="register"),
   path('login/', login_page, name="login"),
   path('logout/', logout, name="logout"),
   path('profile/', profile, name="profile"),
]
