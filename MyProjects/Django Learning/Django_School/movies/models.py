from datetime import date

from django.db import models
from django.urls import reverse


class Category(models.Model):
    '''Categories'''
    name = models.CharField('Category', max_length=150)
    description = models.TextField('Description')
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Actor(models.Model):
    '''Actors and Directors'''
    name = models.CharField('Name', max_length=100)
    age = models.PositiveSmallIntegerField('Age', default=0)
    description = models.TextField('Description')
    image = models.ImageField('Image', upload_to='actors/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('actor_detail', kwargs={'slug': self.name})

    class Meta:
        verbose_name = 'Actors and Directors'
        verbose_name_plural = 'Actors and Directors'


class Genre(models.Model):
    '''Genres'''
    name = models.CharField('Name', max_length=100)
    description = models.TextField('Description')
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class Movie(models.Model):
    '''Movies'''
    title = models.CharField('Title', max_length=100)
    tagline = models.CharField('Tagline', max_length=100, default='')
    description = models.TextField('Description')
    poster = models.ImageField('Image', upload_to='movie/')
    year = models.PositiveSmallIntegerField('Release date', default=2023)
    country = models.CharField('Country', max_length=30)
    directors = models.ManyToManyField(Actor, verbose_name='director', related_name='film_director')
    actors = models.ManyToManyField(Actor, verbose_name='actors', related_name='film_actors')
    genres = models.ManyToManyField(Genre, verbose_name='genre')
    world_premiere = models.DateField('World premiere', default=date.today)
    budget = models.PositiveSmallIntegerField('Budget', default=0, help_text='in US dollars')
    fees_in_usa = models.PositiveSmallIntegerField('Fees in USA', default=0, help_text='in US dollars')
    fees_in_world = models.PositiveSmallIntegerField('Fees in the World', default=0, help_text='in US dollars')
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField('Draft', default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'slug': self.url})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'


class MovieShots(models.Model):
    '''Shots from a Movie'''
    title = models.CharField('Title', max_length=100)
    description = models.TextField('Description')
    image = models.ImageField('Image', upload_to='movie_shots/')
    movie = models.ForeignKey(Movie, verbose_name='Movie', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Shot from a movie'
        verbose_name_plural = 'Shots from a movie'


class RatingStar(models.Model):
    '''Rating Star'''
    value = models.SmallIntegerField('Value', default=0)

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = 'Rating star'
        verbose_name_plural = 'Rating stars'
        ordering = ['-value']


class Rating(models.Model):
    '''Rating'''
    ip = models.CharField('IP-Address', max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='Star')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='Movie')

    def __str__(self):
        return f'{self.star} - {self.movie}'

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'


class Reviews(models.Model):
    '''Reviews'''
    email = models.EmailField()
    name = models.CharField('Name', max_length=100)
    text = models.TextField('Review', max_length=5000)
    parent = models.ForeignKey('self', verbose_name='Parent', on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name='Movie', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.movie}'

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
