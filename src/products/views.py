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
def eScooter_page(request):
   qs = Product.objects.filter(slug__icontains='eScooter')
   template_name = "eScooters.html"
   context = {"eScooters_products": qs}
   return render(request, template_name, context)


# Render only eScooters
def kid_scooter_page(request):
   qs = Product.objects.filter(slug__icontains='kid-scooter')
   template_name = "kid_scooters.html"
   context = {"kid_scooters_products": qs}
   return render(request, template_name, context)
