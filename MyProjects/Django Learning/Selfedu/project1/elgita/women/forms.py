from django import forms
from django.core.exceptions import ValidationError

from .models import *

class AddPostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Not chosen'
    class Meta:
        model = Women
        # fields = '__all__'
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError('Length more than 50 symbols')

        return title