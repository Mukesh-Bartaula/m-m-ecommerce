from django.shortcuts import render
from django.db.models import Q
from products.models import Product


# Create your views here.
def search(request):
    query = request.GET.get("q")
    query2 = request.GET.get("color")

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) or Q(height__icontains=query)
        )
        search_for = query
    if query2:
        products = Product.objects.filter(Q(color__icontains=query2))
        search_for = query2
    if products.exists():
        filter_products = products
    else:
        filter_products = products
    # filter_products = Product.objects.filter(featured=True)

    context = {"products": filter_products, "search_for": search_for}
    return render(request, "search/view.html", context)
