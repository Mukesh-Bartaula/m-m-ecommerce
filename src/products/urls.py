from django.urls import path
from .views import products, product_detail, ProductListView

urlpatterns = [
    # path("", products),
    path("", ProductListView.as_view(), name="product_list"),
    path("detail/<int:id>/", product_detail, name="product_detail"),
]
