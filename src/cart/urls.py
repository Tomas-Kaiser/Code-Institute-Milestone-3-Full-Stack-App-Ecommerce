from django.urls import path

from .views import (
   cart_page,
   add_to_cart,
   edit_cart,
)

urlpatterns = [
   path('', cart_page, name="cart"),
   path('add/<int:id>', add_to_cart, name="add-to-cart"),
   path('edit/<int:id>', edit_cart, name="edit-cart"),

]