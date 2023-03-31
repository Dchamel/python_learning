from django.shortcuts import render
from products.models import *


def one_product(request, product_cat, product_id):
    product = Products.objects.get(id=product_id)
    return render(request, 'products/product.html', locals())
