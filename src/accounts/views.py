from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

# Create your views here.

def register_page(request):
   form = UserRegistrationForm(request.POST or None)
   if form.is_valid():
      form.save()
      return redirect('home')
   context = {
      "register": True,
      "form": form,
   }
   return render(request, 'register.html', context)
