from decimal import Decimal

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Product(models.Model):
    title = models.CharField('Product', max_length=100)
    price = models.DecimalField('Price', max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.title

    def get_discount_price(self):
        return self.price * Decimal(0.8)
    

class Order(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    country = models.CharField('Country', max_length=50, null=True)
    country_id = models.IntegerField('Country ID', null=True)

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'

    def __str__(self):
        return self.user


class OrderItem(models.Model):
    product = models.ForeignKey(Product, verbose_name='Product', on_delete=models.CASCADE, related_name='order_items')
    quantity = models.IntegerField('Quantity')
    order = models.ForeignKey(Order, verbose_name='Order', on_delete=models.CASCADE, related_name='order_items')

    class Meta:
        verbose_name = 'order item'
        verbose_name_plural = 'order items'

    def __str__(self):
        return self.product.title


class Shop(models.Model):
    title = models.CharField('Title', max_length=100)
    address = models.CharField('Address', max_length=200)
    product = models.ManyToManyField(Product, verbose_name='Product', related_name='shops')

    

    

