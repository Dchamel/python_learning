from django.urls import path
from .views import HomeView, ProductView, CategoryView, save_order, work

urlpatterns = [
    # path('', HomeView.as_view(), name='products'),
    path('', work),
    path('product/<int:pk>/', ProductView.as_view(), name='product_detail'),
    path('category/<int:pk>/', CategoryView.as_view(), name='category_detail'),
    path('save_order', save_order),
]
