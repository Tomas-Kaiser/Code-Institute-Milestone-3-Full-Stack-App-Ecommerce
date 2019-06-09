from django.shortcuts import render, get_object_or_404

from .models import Product

def kick_scooter_page(request):
   qs = Product.objects.all()
   template_name = "kick_scooter.html"
   context = {"kick_scooters_products": qs}
   return render(request, template_name, context)

def kick_scooter_detail(request, slug):
   qs = get_object_or_404(Product, slug=slug)
   template_name = "kick_scooter_detail.html"
   context = {"kick_scooter_detail": qs}
   return render(request, template_name, context)
