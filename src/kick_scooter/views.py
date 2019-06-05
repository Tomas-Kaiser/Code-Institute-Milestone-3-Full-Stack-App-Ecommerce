from django.shortcuts import render

# Create your views here.
def kick_scooter_page(request):
   return render(request, 'kick_scooter.html', {})

