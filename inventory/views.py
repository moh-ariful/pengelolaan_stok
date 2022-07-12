from django.shortcuts import get_object_or_404, redirect, render

from inventory.forms import LaptopForm
from .models import *
from .forms import *

# Create your views here.


def index(request):
    return render(request, "index.html")


def display_laptops(request):
    items = Laptop.objects.all()
    context = {
        "items": items,
        "header": "Laptops",
    }
    return render(request, "index.html", context)


def display_desktops(request):
    items = Desktop.objects.all()
    context = {
        "items": items,
        "header": "Desktops",
    }
    return render(request, "index.html", context)


def display_mobiles(request):
    items = Mobile.objects.all()
    context = {
        "items": items,
        "header": "Mobiles",
    }
    return render(request, "index.html", context)


def add_laptop(request):
    if request.method == "POST":
        form = LaptopForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")

    else:
        form = LaptopForm()
        return render(request, "add_new.html", {"form": form})


def add_desktop(request):
    if request.method == "POST":
        form = DesktopForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")

    else:
        form = DesktopForm()
        return render(request, "add_new.html", {"form": form})


def add_mobile(request):
    if request.method == "POST":
        form = MobileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")

    else:
        form = MobileForm()
        return render(request, "add_new.html", {"form": form})


def edit_laptop(request, pk):
    item = get_object_or_404(Laptop, pk=pk)

    if request.method == "POST":
        form = LaptopForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("index")

    else:
        form = LaptopForm(instance=item)

        return render(request, "edit_item.html", {"form": form})


def edit_desktop(request, pk):
    item = get_object_or_404(Desktop, pk=pk)

    if request.method == "POST":
        form = DesktopForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("index")

    else:
        form = DesktopForm(instance=item)

        return render(request, "edit_item.html", {"form": form})


def edit_mobile(request, pk):
    item = get_object_or_404(Mobile, pk=pk)

    if request.method == "POST":
        form = MobileForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("index")

    else:
        form = MobileForm(instance=item)

        return render(request, "edit_item.html", {"form": form})


def delete_laptop(request, pk):

    Laptop.objects.filter(id=pk).delete()

    items = Laptop.objects.all()

    context = {"items": items}

    return render(request, "index.html", context)


def delete_desktop(request, pk):

    Desktop.objects.filter(id=pk).delete()

    items = Desktop.objects.all()

    context = {"items": items}

    return render(request, "index.html", context)


def delete_mobile(request, pk):

    Mobile.objects.filter(id=pk).delete()

    items = Mobile.objects.all()

    context = {"items": items}

    return render(request, "index.html", context)
