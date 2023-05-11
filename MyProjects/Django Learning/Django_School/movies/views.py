from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Movie


class MoviesView(ListView):
    '''All Films'''
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    # template_name = 'movies/movie_list.html'


class MovieDetailView(DetailView):
    '''One Film'''
    model = Movie
    slug_field = 'url'

    # def get(self, request, slug):
    #     movie = Movie.objects.get(url=slug)
    #     return render(request, 'movies/movie_detail.html', {'movie': movie})
