from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Page of Women App')

def categories(request):
    return HttpResponse('<h1>Pages by Categories</h1>')