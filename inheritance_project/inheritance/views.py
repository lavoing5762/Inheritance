
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse 
from inheritance.forms import ImageForm

# Create your views here.

def landingpage(request):
    return render(request,'landingpage.html')

def ourstory(request):
    return render(request,'ourstory.html')

# This calls the image form and renders the image upload on add artifact page 
def addartifact(request):
    # return render(request,'addartifact.html')
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'addartifact.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'addartifact.html', {'form': form})

def gallery(request):
    return render(request,'gallery.html')



