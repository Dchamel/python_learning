# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.db.models.functions import Length
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.db.models import *

from .forms import *
from .models import *
from .utils import *

from django.contrib.auth.mixins import LoginRequiredMixin


class WomenHome(DataMixin, ListView):
    # model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Women.objects.filter(is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Main Page')
        return dict(list(context.items()) + list(c_def.items()))


# def index(request):
#     posts = Women.objects.all()
#
#     context = {
#         'posts': posts,
#         'title': 'Main page',
#         'cat_selected': 0,
#     }
#     return render(request, 'women/index.html', context=context)

# @login_required
def about(request):
    contact_list = Women.objects.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'women/about.html', {'page_obj': page_obj, 'menu': menu, 'title': 'About us'})


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    # success_url = reverse_lazy('home')
    # login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Add Article')
        return dict(list(context.items()) + list(c_def.items()))


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

# def contact(request):
#     return HttpResponse('Feedback')

class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'women/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Register')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


# def login(request):
#     return HttpResponse('Login')

class ShowPost(DataMixin, DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


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

class WomenCategory(DataMixin, ListView):
    # model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Category- ' + str(c.name),
                                      cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))


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
    data.append(Women.objects.filter(pk__in=[1, 3, 4]))
    data += '-'
    try:
        data.append(Women.objects.filter(pk__in=[1, 3, 4]), is_published=False)
    except:
        data.append('None')
    data += '-'
    data.append(Women.objects.filter(cat__in=[1, 2]))
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
    data.append(Women.objects.count())
    data += '-'
    data.append(Women.objects.aggregate(Min('cat_id')))
    data += '-'
    data.append(Women.objects.aggregate(Min('cat_id'), Max('cat_id')))
    data += '-'
    data.append(Women.objects.aggregate(min=Min('cat_id'), max=Max('cat_id')))
    data += '-'
    data.append(Women.objects.aggregate(res=Min('id') - Max('id')))
    data += '-'
    data.append(Women.objects.aggregate(res=Avg("id")))
    data += '-'
    data.append(Women.objects.filter(pk__gt=4).aggregate(res=Avg('id')))
    data += '-'
    data.append(Women.objects.values('title', 'cat_id').get(pk=1))
    data += '-'
    data.append(Women.objects.values('title', 'cat__name').get(pk=1))
    data += '-'
    # Group By
    data.append(Women.objects.values(category=F('cat_id')).annotate(count=Count('id')))
    data += '-'
    data.append(Category.objects.annotate(total=Count('women')).filter(total__gte=4))
    data += '-'
    data.append(Women.objects.filter(pk__gt=F('cat_id')))
    data += '-'
    len11 = Women.objects.annotate(len=Length('title'))
    data += (item.title + ' ' + str(item.len) for item in len11)
    data += '-'
    q01 = Women.objects.raw('SELECT id, title from women_women')
    data += (str(each.id) + ' ' + each.title for each in q01)
    data += '-'
    q02 = Women.objects.raw('SELECT id, title FROM women_women WHERE slug="halle-berry"')
    data += q02
    data += '-'
    # WARNING right way to sql-injections
    slug01 = 'pink'
    q03 = Women.objects.raw(f'SELECT id, title FROM women_women WHERE slug="{slug01}"')
    data += q03
    data += '-'
    # Simple protection against sql-injections
    q04 = Women.objects.raw('SELECT id, title FROM women_women WHERE slug=%s', [slug01])
    data += q04
    data += '-'

    return render(request, 'women/ormlearning.html', {'data': data})


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'women/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Register')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'women/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Login')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')
