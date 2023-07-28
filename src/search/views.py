from django.shortcuts import render
from django.db.models import Q
from products.models import Product


# Create your views here.
def search(request):
    query = request.GET.get("q")
    products = Product.objects.filter(Q(name__icontains=query))
    search_for = query
    if products.exists():
        filter_products = products
    else:
        filter_products = products
    # filter_products = Product.objects.filter(featured=True)

    context = {"products": filter_products, "search_for": search_for}
    return render(request, "search/view.html", context)
