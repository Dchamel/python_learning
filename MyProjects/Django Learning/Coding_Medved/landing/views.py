from django.shortcuts import render
from .forms import SubscriberForm


def landing(request):
    name = 'CodingMedved'
    form = SubscriberForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()

    return render(request, 'landing/landing.html', locals())
