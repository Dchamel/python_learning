from django.shortcuts import render
from django.http import HttpResponse


def product_list(request):
    return render(request, 'store/product_list.html', context={'product_title': 'Range Rover'})
