from typing import Any, Dict
from django.db.models import Q
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView
from .models import Product


def products(request):
    products = Product.objects.exclude(name__icontains="T-shirt")
    template = loader.get_template("home.html")
    context = {"products": products}
    return HttpResponse(template.render(context, request))


class ProductListView(ListView):
    model = Product
    template_name = "home.html"
    context_object_name = "products"


def product_detail(request, id):
    product = Product.objects.get(id=id)
    # context = {
    #     "id": request.GET.get("p_id"),
    #     "product_detail": Product.objects.filter(id=id),
    # }
    context = {"product": product}
    return render(request, "product_detail.html", context)
