from django.http import HttpResponse
from django.shortcuts import render
# from .models import MyModel

# def HomePage(request):
#     return HttpResponse("Hello, welcome to the home page!")

def HomePage(request):    
 data = {
        "title":"Home New",
        }
 return render(request,"home.html",data , )  # render kar denege 
