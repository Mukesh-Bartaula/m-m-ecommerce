from django.shortcuts import render
from .models import Cart


def cart(request):
    cart, _ = Cart.objects.new_or_get(request)
    products = cart.products.all()
    request.session["item_count"] = products.count()
    context = {"cart": cart, "products": products}
    return render(request, "table_cart.html", context)
