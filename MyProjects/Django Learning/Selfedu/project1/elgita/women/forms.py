from django import forms
from .models import *

class AddPostForm(forms.Form):
    title = forms.CharField(max_length=25, label='Woman`s name')
    slug = forms.SlugField(max_length=255, label='URL')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Biography')
    is_published = forms.BooleanField(label='Publish now ?', required=False, initial=True)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Category', empty_label='Not chosen')