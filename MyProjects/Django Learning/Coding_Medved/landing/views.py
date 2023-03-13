from django.shortcuts import render
from .forms import SubscriberForm


def landing(request):
    name = 'CodingMedved'
    form = SubscriberForm(request.POST or None)
    return render(request, 'landing/landing.html', locals())
