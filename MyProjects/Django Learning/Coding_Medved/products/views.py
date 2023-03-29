from django.shortcuts import render
from products.models import *


def product(request, product_cat, product_id):
    product_id = Products.objects.get(id=product_id)
    product_cat = Products.objects.get(category=product_cat)
    return render(request, 'products/product.html', locals())
