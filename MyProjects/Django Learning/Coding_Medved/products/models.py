from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ProductImage(models.Model):
    product = models.ForeignKey(Products, blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
