from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

def index(request):
    return HttpResponse('Page of Women App')

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