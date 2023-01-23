from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *

menu = ['About', 'Add Article', 'Feedback', 'Sign in']
def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Main page'})

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'About us'})

def categories(request, catid):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Pages by Categories</h1><p>{catid}</p>')

def archive(request, year):
    if int(year) > 2024:
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1>Archive by years</h1><p>{year}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>page not found</h1>')