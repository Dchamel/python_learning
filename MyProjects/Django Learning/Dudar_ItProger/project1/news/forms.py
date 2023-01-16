from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'preview', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }),
            'preview': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Preview'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Input your text'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date'
            })
        }