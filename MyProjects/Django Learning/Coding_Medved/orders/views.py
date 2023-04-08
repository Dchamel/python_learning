from django.http import JsonResponse
from .models import ProductInBasket


def basket_adding(request):
    return_dict = dict()

    session_key = request.session.session_key
    print(request.POST)

    ProductInBasket.objects.get(session_key=session_key)

    return JsonResponse(return_dict)
