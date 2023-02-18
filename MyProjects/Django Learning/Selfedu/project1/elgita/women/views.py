from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Q

from .forms import *
from .models import *

menu = [{'title': "About", 'url_name': 'about'},
        {'title': "Add Article", 'url_name': 'add_page'},
        {'title': "Feedback", 'url_name': 'contact'},
        {'title': "Login", 'url_name': 'login'}
]

class WomenHome(ListView):
    # model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Women.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Main page'
        context['cat_selected'] = 0
        return context

# def index(request):
#     posts = Women.objects.all()
#
#     context = {
#         'posts': posts,
#         'title': 'Main page',
#         'cat_selected': 0,
#     }
#     return render(request, 'women/index.html', context=context)

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'About us'})

class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    # success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Page'
        return context

# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             # try:
#             #     Women.objects.create(**form.cleaned_data)
#             #     return redirect('home')
#             # except:
#             #     form.add_error(None, 'Error while add an Article')
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     return render(request, 'women/addpage.html', {'form': form, 'menu': menu, 'title': 'Add Article'})

def contact(request):
    return HttpResponse('Feedback')

def login(request):
    return HttpResponse('Login')

class ShowPost(DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'


# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id
#     }
#
#     return render(request, 'women/post.html', context=context)

class WomenCategory(ListView):
    # model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = f'Category - {str(context["posts"][0].cat)}'
        context['cat_selected'] = context['posts'][0].cat_id
        return context

# def show_category(request, cat_slug):
#     cat_id = get_object_or_404(Category, slug=cat_slug).id
#     posts = Women.objects.filter(cat_id=cat_id)
#
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {
#         'posts': posts,
#         'title': 'All Categories',
#         'cat_selected': cat_slug,
#     }
#     return render(request, 'women/index.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>page not found</h1>')

def ormlearning(request):
    data = []
    data += Women.objects.all()
    data += '-'
    data += Women.objects.all()[:2]
    data += '-'
    data += Women.objects.order_by('-pk')[:2]
    data += '-'
    # the same
    data += Women.objects.order_by('pk').reverse()[:2]
    data += '-'
    data += Women.objects.filter(pk__lte=2)
    data += '-'
    data.append(Women.objects.get(pk=1))
    data += '-'
    data.append(Women.objects.get(pk=1).cat)
    data += '-'
    data.append(Women.objects.get(pk=1).cat.slug)
    data += '-'
    data.append(Category.objects.get(pk=1).women_set.all())
    data += '-'
    data.append(Women.objects.filter(pk__gte=2))
    data += '-'
    data.append(Women.objects.filter(title__contains='av'))
    data += '-'
    data.append(Women.objects.filter(pk__in=[1,3,4]))
    data += '-'
    try:
        data.append(Women.objects.filter(pk__in=[1, 3, 4]), is_published=False)
    except:
        data.append('None')
    data += '-'
    data.append(Women.objects.filter(cat__in=[1,2]))
    data += '-'
    data.append(Women.objects.filter(cat__in=Category.objects.all()))
    data += '-'
    data.append(Women.objects.filter(pk__lt=3, cat_id=1))
    data += '-'
    # or by Q
    data.append(Women.objects.filter(Q(pk__lt=3) | Q(cat_id=1)))
    data += '-'
    # and by Q
    data.append(Women.objects.filter(Q(pk__lt=3) & Q(cat_id=1)))
    data += '-'
    # not by Q
    data.append(Women.objects.filter(~Q(pk__lt=3) & Q(cat_id=1)))
    data += '-'
    data.append(Women.objects.first())
    data += '-'
    data.append(Women.objects.order_by('-pk').first())
    data += '-'
    data.append(Women.objects.last())
    data += '-'
    data.append(Women.objects.latest('time_create'))
    data += '-'
    data.append(Women.objects.order_by('-time_create'))
    data += '-'
    data.append(Women.objects.earliest('time_create'))
    data += '-'
    data.append(Women.objects.get(pk=4).get_previous_by_time_update())
    data += '-'
    data.append(Women.objects.get(pk=4).get_previous_by_time_update(pk__lte=2))
    data += '-'
    data.append(Category.objects.get(pk=3).women_set.exists())
    data += '-'
    data.append(Category.objects.get(pk=1).women_set.count())
    data += '-'
    data.append(Women.objects.filter(pk__gte=2).count())
    data += '-'
    data.append(Women.objects.filter(cat__slug='actors'))
    data += '-'
    data.append(Women.objects.filter(cat__in=[2]))
    data += '-'
    data.append(Women.objects.filter(cat__name__contains='ct'))
    data += '-'
    data.append(Category.objects.filter(women__title__contains='ma'))
    data += '-'
    data += '-'
    data += '-'
    data += '-'
    data += '-'
    data += '-'
    data += '-'
    data += '-'
    data += '-'
    data += '-'
    data += '-'
    data += '-'
    data += '-'
    data += '-'


    return render(request, 'women/ormlearning.html',{'data':data})