from django.db import models

from products.models import Products


class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return 'Status %s' % self.name

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'


class Orders(models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    customer_name = models.CharField(max_length=50, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    customer_address = models.CharField(max_length=128, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return 'Order %s %s' % (self.id, self.status.name)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class ProductInOrder(models.Model):
    order = models.ForeignKey(Orders, blank=True, null=True, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, blank=True, null=True, default=None, on_delete=models.CASCADE)
    number = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '%s' % self.product.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
