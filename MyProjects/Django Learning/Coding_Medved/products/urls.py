from django.urls import path
from products import views

urlpatterns = [
    path('<slug:product_cat>/<int:product_id>', views.one_product, name='product'),
]
