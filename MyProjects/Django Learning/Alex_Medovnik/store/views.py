from django.shortcuts import render
from django.http import HttpResponse


def build_template(lst: list, cols: int) -> list:
    new_list = []
    for i in range(0, len(lst), cols):
        new_list.append(lst[i:i + cols])
    return new_list


print(build_template([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))


def product_list(request):
    products = [
        {'title': 'Range Rover', 'Info': 'lorem ipsum...', 'price': 10000},
        {'title': 'Land Rover', 'Info': 'lorem ipsum...', 'price': 8000},
        {'title': 'Range Rover Sport', 'Info': 'lorem ipsum...', 'price': 12000},
    ]

    return render(request, 'store/product_list.html',
                  context={'products': products})
