from django.shortcuts import render
from . models import Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request,'plp_commerce/product-list.html',context)