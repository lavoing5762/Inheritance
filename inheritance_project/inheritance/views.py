from django.shortcuts import render
from django.urls import reverse 

# Create your views here.

def landingpage(request):
    return render(request,'landingpage.html')

def ourstory(request):
    return render(request,'ourstory.html')

def addartifact(request):
    return render(request,'addartifact.html')

def gallery(request):
    return render(request,'gallery.html')

