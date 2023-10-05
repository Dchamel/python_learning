from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.views.generic import ListView, DetailView

from .models import *


# def build_template(lst: list, cols: int) -> list:
#     return [lst[i:i + cols] for i in range(0, len(lst), cols)]

class HomeView(ListView):
    model = Product

    def get_queryset(self):
        search_query = self.request.GET.get('search', None)
        if search_query:
            return self.model.objects.filter(
                Q(title__icontains=search_query) | Q(info__icontains=search_query)
            )
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ProductView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class CategoryView(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


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
