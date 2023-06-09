from django.contrib import admin
from django import forms

from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from modeltranslation.admin import TranslationAdmin

from .models import *


class MovieAdminForm(forms.ModelForm):
    # here we put field from our Model where do we need to see the editor
    description_ru = forms.CharField(label='Description CKEditor RU', widget=CKEditorUploadingWidget())
    description_en = forms.CharField(label='Description CKEditor EN', widget=CKEditorUploadingWidget())

    class Meta:
        model = Movie
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    '''Categories'''
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


class ReviewInline(admin.TabularInline):
    '''Reviews at the Film page'''
    model = Reviews
    extra = 1
    readonly_fields = ('email', 'name')


class MovieShotsInLine(admin.TabularInline):
    model = MovieShots
    extra = 1

    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="120"')

    get_image.short_description = 'Image'


@admin.register(Movie)
class MovieAdmin(TranslationAdmin):
    '''Films'''
    list_display = ('title', 'category', 'url', 'draft')
    list_filter = ('category', 'year')
    search_fields = ('title', 'category__name')
    inlines = [MovieShotsInLine, ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ('draft',)
    actions = ['publish', 'unpublish']
    form = MovieAdminForm
    # fields = (('actors', 'directors', 'genres'),)
    fieldsets = (
        (None, {
            'fields': (('title', 'tagline'),)
        }),
        (None, {
            'fields': ('description', ('poster', 'get_image'))
        }),
        (None, {
            'fields': (('year', 'world_premiere', 'country'),)
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

    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="120"')

    get_image.short_description = 'Image'

    def unpublish(self, request, queryset):
        '''Mass Unpublish'''
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = '1 movie has been changed'
        else:
            message_bit = f'{row_update} movies had been changed'
        self.message_user(request, f'{message_bit}')

    def publish(self, request, queryset):
        '''Mass Publish'''
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = '1 movie has been changed'
        else:
            message_bit = f'{row_update} movies had been changed'
        self.message_user(request, f'{message_bit}')

    publish.short_description = 'Publish'
    publish.allowed_permissions = ('change',)

    unpublish.short_description = 'Unpublish'
    unpublish.allowed_permissions = ('change',)


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    '''Reviews'''
    list_display = ('name', 'email', 'parent', 'movie', 'id')
    readonly_fields = ('name', 'email')


@admin.register(Genre)
class GenreAdmin(TranslationAdmin):
    '''Genres'''
    list_display = ('name', 'url')


@admin.register(Actor)
class ActorAdmin(TranslationAdmin):
    '''Actors'''
    list_display = ('name', 'age', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = 'Image'


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    '''Review'''
    list_display = ('movie', 'star', 'ip')


@admin.register(MovieShots)
class MovieShotsAdmin(TranslationAdmin):
    '''Shots from a Movie'''
    list_display = ('title', 'movie', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = 'Image'


admin.site.register(RatingStar)

admin.site.site_title = 'Django Movies'
admin.site.site_header = 'Django Movies'


class FlatPagesAdminCustom(FlatPageAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget}
    }


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPagesAdminCustom)
