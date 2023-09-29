from django.shortcuts import render
from django.http import HttpResponse

from .models import *


def build_template(lst: list, cols: int) -> list:
    return [lst[i:i + cols] for i in range(0, len(lst), cols)]


def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    return render(request, 'store/product_list.html', context={
        'product_list': build_template(products, 3),
        'categories': categories,
    })


def product_detail(request, pk):
    categories = Category.objects.all()
    product = Product.objects.get(pk=pk)

    return render(request, 'store/product_detail.html', context={
        'categories': categories,
        'product': product,
    })


def category_detail(request, pk):
    categories = Category.objects.all()
    category = Category.objects.get(pk=pk)
    products = category.products.all()

    return render(request, 'store/category_detail.html', context={
        'product_list': build_template(products, 3),
        'categories': categories,
        'category': category,
    })
