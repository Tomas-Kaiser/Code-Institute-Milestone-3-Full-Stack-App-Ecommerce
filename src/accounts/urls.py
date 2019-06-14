from django.urls import path
from .views import (
   register_page,
   login_page,
   logout,
)

urlpatterns = [
   path('register/', register_page, name="register"),
   # path('login/',),
   path('login/', login_page, name="login"),
   path('logout/', logout, name="logout"),
]
