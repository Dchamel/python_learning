from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Categories'''
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


class ReviewInline(admin.TabularInline):
    '''Reviews at the Film page'''
    model = Reviews
    extra = 1
    readonly_fields = ('email', 'name')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    '''Films'''
    list_display = ('title', 'category', 'url', 'draft')
    list_filter = ('category', 'year')
    search_fields = ('title', 'category__name')

    inlines = [ReviewInline]

    save_on_top = True

    save_as = True

    list_editable = ('draft',)
    # fields = (('actors', 'directors', 'genres'),)
    fieldsets = (
        (None, {
            'fields': (('title', 'tagline'),)
        }),
        (None, {
            'fields': ('description', 'poster')
        }),
        (None, {
            'fields': (('year', 'country'),)
        }),
        ('Directors/Actors/Genres', {
            'classes': ('collapse',),
            'fields': ('actors', 'directors', 'genres', 'category')
        }),
        (None, {
            'fields': (('budget', 'fees_in_usa', 'fees_in_world'),)
        }),
        ('Options', {
            'fields': (('url', 'draft'),)
        }),
    )


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    '''Reviews'''
    list_display = ('name', 'email', 'parent', 'movie', 'id')
    readonly_fields = ('name', 'email')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    '''Genres'''
    list_display = ('name', 'url')


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    '''Actors'''
    list_display = ('name', 'age')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    '''Review'''
    list_display = ('movie', 'star', 'ip')


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    '''Shots from a Movie'''
    list_display = ('title', 'movie')
