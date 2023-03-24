from django.shortcuts import render
from .forms import SubscriberForm
from products.models import Products


def landing(request):
    name = 'CodingMedved'
    form = SubscriberForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()

    return render(request, 'landing/landing.html', locals())


def home(request):
    products = Products.objects.filter(is_active=True)
    return render(request, 'landing/home.html', locals())
