from django.shortcuts import render
from rest_framework import generics
from myshop.serializers import OrderSerializer, ProductSerializer
from myshop.models import Product, Order


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializer


class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer


class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()