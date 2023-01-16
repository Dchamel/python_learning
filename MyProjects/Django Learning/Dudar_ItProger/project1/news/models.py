from django.db import models

class Articles(models.Model):
    title = models.CharField('Title', max_length=50)
    preview = models.CharField('Preview', max_length=250)
    full_text = models.TextField('Article')
    date = models.DateTimeField('Date')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'