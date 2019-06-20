from django.shortcuts import render, get_object_or_404, redirect
import stripe
from .forms import OrderForm, PaymentForm
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from products.models import Product
from .models import OrderLineItem

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET

def checkout(request):
   print("THis is request.POST ")
   print(request.POST)
   order_form = OrderForm(request.POST or None)
   payment_form = PaymentForm(request.POST or None)

   if order_form.is_valid() and payment_form.is_valid():
      order = order_form.save(commit=False)
      order.date = timezone.now()
      order.save()

      cart = request.session.get('cart', {})
      total = 0
      for id, quantity in cart.items():
         product = get_object_or_404(Product, pk=id)
         total += quantity * product.price
         order_line_item = OrderLineItem(
            order = order,
            product = product,
            quantity = quantity
         )
         order_line_item.save()

      try:
         customer = stripe.Charge.create(
            amount = int(total * 100),
            currency = "EUR",
            description = request.user.email,
            card = payment_form.cleaned_data['stripe_id']
         )
      except stripe.error.CardError:
         messages.error(request, "Your card was declined")

      if customer.paid:
         messages.error(request, "You have successfully paid")
         request.session['cart'] = {}
         return redirect('home')
      else:
         messages.error(request, "Unable o take payment")
   else:
      print(payment_form.errors)
      messages.error(request, "We were unable to take a payment with that card!")

   context = {
      'order_form': order_form,
      'payment_form': payment_form,
      'publishable': settings.STRIPE_PUBLISHABLE
   }

   return render(request, "checkout.html", context)

