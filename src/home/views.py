from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def index_page(request):
   my_title = "Home page"
   context  = {"title": my_title}
   return render(request, "home.html", context)
