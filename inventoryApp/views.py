from multiprocessing import context
from django.shortcuts import get_object_or_404, redirect, render
from inventoryApp.forms import *

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

def edit_device(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == 'POST':
        form = cls(request.POST, instance=item)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = cls(instance=item)
        return render(request, 'edit_item.html', {'form': form})

def edit_laptops(request, pk):
    return edit_device(request, pk, Laptop, LaptopForm)

def edit_desktops(request, pk):
    return edit_device(request, pk, Desktop, DesktopForm)

def edit_mobiles(request, pk):
    return edit_device(request, pk, Mobile, MobileForm)


def delete_laptops(request, pk):
    Laptop.objects.filter(id=pk).delete()
    items = Laptop.objects.all()
    context = {
        'items' : items
    }

    return render(request, 'home.html', context)

def delete_desktops(request, pk):
    Desktop.objects.filter(id=pk).delete()
    items = Desktop.objects.all()
    context = {
        'items' : items
    }

    return render(request, 'home.html', context)

def delete_mobiles(request, pk):
    Mobile.objects.filter(id=pk).delete()
    items = Mobile.objects.all()
    context = {
        'items' : items
    }

    return render(request, 'home.html', context)
