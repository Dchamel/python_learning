from django.urls import path
from .views import product_list

urlpatterns = [
    path('store/', product_list),
    path('detail/', product_list),
]
