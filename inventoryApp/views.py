from django.shortcuts import render

from inventoryApp.models import *

# Create your views here.

def Home(request):
    return render(request, 'home.html')

def display_laptops(request):
    items = Laptop.objects.all()
    context = {
        'items' : items,
        'header' : 'Laptops'
    }

    return render(request, 'home.html', context)

def display_desktops(request):
    items = Desktop.objects.all()
    context = {
        'items' : items,
        'header' : 'Desktops'
    }

    return render(request, 'home.html', context)

def display_mobiles(request):
    items = Mobile.objects.all()
    context = {
        'items' : items,
        'header' : 'Mobiles'
    }

    return render(request, 'home.html', context)
