from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.views.generic import ListView, DetailView
from .utils import CategoriesMixin

from .models import *

from django.http import HttpResponse


def work(request):
    # p = Product(title='Ford', price=2654)
    # p.save()
    # p = Product.objects.create(title='Lexux', price=348957)

    p = Product.objects.get(title='Lexux')
    p.price -= 100000
    obj = Product.objects.all()
    print(p.price)
    return HttpResponse('Hello')


# def build_template(lst: list, cols: int) -> list:
#     return [lst[i:i + cols] for i in range(0, len(lst), cols)]


class HomeView(ListView, CategoriesMixin):
    model = Product

    def get_queryset(self):
        search_query = self.request.GET.get('search', None)
        if search_query:
            return self.model.objects.filter(
                Q(title__icontains=search_query) | Q(info__icontains=search_query)
            )
        return self.model.objects.all()


class ProductView(DetailView, CategoriesMixin):
    model = Product


class CategoryView(DetailView, CategoriesMixin):
    model = Category


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
