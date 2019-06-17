from django.shortcuts import render,redirect

# Create your views here.

def cart_page(request):
   """
   A view that renders the cart contents page
   """
   return render(request, "cart.html")


def add_to_cart(request, id):
   """
   Add a quantity of the specified product to the cart
   """
   quantity = int(request.POST['quantity'])

   cart = request.session.get('cart', {})
 
   if id in cart:
      cart[id] = int(cart[id]) + quantity      
   else:
      cart[id] = cart.get(id, quantity) 

   request.session['cart'] = cart

   return redirect('home')


def edit_cart(request, id):
   """
   Edit the quantity of the specified product to the specified amount
   """
   quantity = int(request.POST['quantity'])
   cart = request.session.get('cart', {})

   if quantity > 0:
      cart[id] = quantity
   else:
      cart.pop(id)

   request.session['cart'] = cart
   
   return redirect('cart')

