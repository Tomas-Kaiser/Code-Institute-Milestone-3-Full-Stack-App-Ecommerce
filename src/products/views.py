from django.shortcuts import render, get_object_or_404

from .models import Product

# Render only kick scooters
def kick_scooter_page(request):
   qs = Product.objects.filter(slug__icontains='kick-scooter')
   template_name = "kick_scooter/kick_scooters.html"
   context = {"kick_scooters_products": qs}
   return render(request, template_name, context)

def kick_scooter_detail(request, slug):
   qs = get_object_or_404(Product, slug=slug)
   print(qs)
   template_name = "kick_scooter/kick_scooter_detail.html"
   context = {"kick_scooter_detail": qs}
   return render(request, template_name, context)


# Render only eScooters
def e_scooter_page(request):
   qs = Product.objects.filter(slug__icontains='eScooter')
   template_name = "e_scooter/e_scooters.html"
   context = {"e_scooters_products": qs}
   return render(request, template_name, context)

def e_scooter_detail(request, slug):
   qs = get_object_or_404(Product, slug=slug)
   template_name = "e_scooter/e_scooter_detail.html"
   context = {"e_scooter_detail": qs}
   return render(request, template_name, context)


# Render only kid scooters
def kid_scooter_page(request):
   qs = Product.objects.filter(slug__icontains='kid-scooter')
   template_name = "kid_scooter/kid_scooters.html"
   context = {"kid_scooters_products": qs}
   return render(request, template_name, context)

def kid_scooter_detail(request, slug):
   qs = get_object_or_404(Product, slug=slug)
   template_name = "kid_scooter/kid_scooter_detail.html"
   context = {"kid_scooter_detail": qs}
   return render(request, template_name, context)
