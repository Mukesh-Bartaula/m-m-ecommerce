from django.shortcuts import render
from django.http import HttpResponseRedirect
from products.models import Product


def home(request):
    context = {"products": Product.objects.all()}
    return render(request, "home.html", context)


def form(request):
    return render(request, "form.html")
