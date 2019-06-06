from django.shortcuts import render
from .models import KickScooters

# Create your views here.
def kick_scooter_page(request):
   qs = KickScooters.objects.all()
   template_name = "kick_scooter.html"
   context = {"kick_scooters_products": qs}
   return render(request, template_name, context)

