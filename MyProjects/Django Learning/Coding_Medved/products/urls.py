from django.contrib import admin
from django.urls import path, include
from products import views

urlpatterns = [
    path('product/<product_cat>/<product_id>', views.product, name='product'),
]
