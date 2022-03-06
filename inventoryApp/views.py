from django.shortcuts import redirect, render
from inventoryApp.forms import DesktopForm, LaptopForm, MobileForm

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


def add_device(request, cls):
    if request.method == 'POST':
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = cls()
        return render(request, 'add_new.html', {'form': form})

def add_laptops(request):
    return add_device(request, LaptopForm)

def add_desktops(request):
    return add_device(request, DesktopForm)

def add_mobiles(request):
    return add_device(request, MobileForm)
