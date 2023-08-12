from django.http import JsonResponse
from django.shortcuts import render
from .models import Cart


def cart(request):
    cart, _ = Cart.objects.new_or_get(request)
    products = cart.products.all()
    request.session["item_count"] = products.count()
    context = {"cart": cart, "products": products}
    return render(request, "table_cart.html", context)


def add_to_cart(request, product_id):
    cart_id = request.session.get("cart_id")
    cart = Cart.objects.get(id=cart_id)
    cart.products.add(product_id)
    return JsonResponse({"success": True})


def remove_from_cart(request, product_id):
    cart_id = request.session.get("cart_id")
    cart = Cart.objects.get(id=cart_id)
    cart.products.remove(product_id)
    
    return JsonResponse({"success": True})
