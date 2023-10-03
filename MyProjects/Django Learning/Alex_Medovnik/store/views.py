from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q

from .models import *


def build_template(lst: list, cols: int) -> list:
    return [lst[i:i + cols] for i in range(0, len(lst), cols)]


def product_list(request):
    categories = Category.objects.all()
    search_query = request.GET.get('search', None)
    if search_query:
        product_list = Product.objects.filter(
            Q(title__icontains=search_query) | Q(info__icontains=search_query)
        )
    else:
        product_list = Product.objects.all()

    return render(request, 'store/product_list.html', context={
        'product_list': product_list,
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
    product_list = category.products.all()

    return render(request, 'store/category_detail.html', context={
        'product_list': product_list,
        'categories': categories,
        'category': category,
    })


def save_order(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    order = Order()
    order.name = request.POST['user_name']
    order.email = request.POST['user_email']
    order.product = Product.objects.get(pk=request.POST['product_id'])
    order.save()

    return render(request, 'store/order.html', context={
        'categories': categories,
        'order': order,
        'prod_price': order.product.price
    })
