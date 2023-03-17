from django.db import models


class Order(models.Model):
    customer_name = models.CharField(max_length=50, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return 'Order %s' % self.id

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class ProductInOrder(models.Model):
    order = models

    customer_name = models.CharField(max_length=50, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return 'Order %s' % self.id

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
