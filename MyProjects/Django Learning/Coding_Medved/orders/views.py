from django.http import JsonResponse
from .models import ProductInBasket


def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST
    product_id = data.get('product_id')
    num = data.get('num')

    new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id,
                                                                 defaults={'number': num})
    if not created:
        new_product.number += int(num)
        new_product.save(force_update=True)

    products_in_cart = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    return_dict['products_total_numb'] = products_in_cart.count()
    return_dict['products'] = list()

    for item in products_in_cart:
        products_dict = dict()
        products_dict['name'] = item.product.name
        products_dict['price_per_item'] = item.price_per_item
        products_dict['num'] = item.number
        return_dict['products'].append(products_dict)

    return JsonResponse(return_dict)
