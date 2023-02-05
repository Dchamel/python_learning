from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *

menu = [{'title': "About", 'url_name': 'about'},
        {'title': "Add Article", 'url_name': 'add_page'},
        {'title': "Feedback", 'url_name': 'contact'},
        {'title': "Login", 'url_name': 'login'}
]
def index(request):
    posts = Women.objects.all()

    context = {
        'posts': posts,
        'title': 'Main page',
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=context)

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'About us'})

def addpage(request):
    return HttpResponse('Add Page')

def contact(request):
    return HttpResponse('Feedback')

def login(request):
    return HttpResponse('Login')

def show_post(request, post_id):
    post = get_object_or_404(Women, pk=post_id)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id
    }

    return render(request, 'women/post.html', context=context)

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'title': 'All Categories',
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>page not found</h1>')