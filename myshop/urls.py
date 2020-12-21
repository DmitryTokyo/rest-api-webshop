from django.urls import path
from myshop.views import (OrderCreateView, ProductCreateView, 
                          ProductListView, ProductDetailView,
                          OrderListView, OrderDetailView)

urlpatterns = [
    path('order/create/', OrderCreateView.as_view()),
    path('orders/all/', OrderListView.as_view()),
    path('order/<int:pk>/', OrderDetailView.as_view()),
    path('product/create/', ProductCreateView.as_view()),
    path('products/all/', ProductListView.as_view()),
    path('product/<int:pk>/', ProductDetailView.as_view()),
]
