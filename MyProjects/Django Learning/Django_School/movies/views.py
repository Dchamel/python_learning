from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Movie
from .forms import ReviewForm


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


class AddReview(View):
    '''Review'''

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            # form.movie_id = pk
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())
