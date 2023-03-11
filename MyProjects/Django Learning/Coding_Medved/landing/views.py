from django.shortcuts import render

def landing(request):
    name = 'CodingMedved'
    return render(request, 'landing/landing.html', locals())
