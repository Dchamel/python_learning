from django.http import JsonResponse
from .models import ProductInBasket


def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST
    product_id = data.get('product_id')
    num = data.get('num')

    new_product = ProductInBasket.objects.create(session_key=session_key, product_id=product_id, number=num)
    products_total_nmb = ProductInBasket.objects.filter(session_key=session_key, is_active=True).count()
    return_dict['products_total_numb'] = products_total_nmb

    return JsonResponse(return_dict)
