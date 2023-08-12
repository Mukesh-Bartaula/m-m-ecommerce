from typing import Iterable, Optional
from django.conf import settings
from django.db import models
from products.models import Product


class CartManager(models.Manager):
    def new_or_get(self, request):
        is_new = False
        cart_id = request.session.get("cart_id", None)
        if cart_id is None:
            # create new cart
            cart_obj = self.new_cart(request.user)
            is_new = True
        else:
            cart_obj = Cart.objects.filter(id=cart_id)
            if cart_obj.count() == 0:
                cart_obj = self.new_cart(request.user)
                is_new = True
            elif cart_obj.count() == 1:
                cart_obj = cart_obj.first()
                if request.user.is_authenticated and cart_obj.user is None:
                    cart_obj.user = request.user
                    cart_obj.save()
        cart_id = cart_obj.id
        request.session["cart_id"] = cart_id

        return cart_obj, is_new

    def new_cart(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)


class Cart(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    products = models.ManyToManyField(Product, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    updated_at = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = CartManager()

    def __str__(self):
        return str(self.id)  #  1

    # def save(self, *args, **kwargs):
    #     total = 0
    #     for product in self.products.all():
    #         total += product.price
    #     self.total = total
    #     return super().save(*args, **kwargs)
