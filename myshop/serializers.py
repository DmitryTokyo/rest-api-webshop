from rest_framework import serializers
from myshop.models import Product, Order, OrderItem, Shop


class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity']


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'title', 'address']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.is_official_reseller:
            representation['official_reseller'] = True
        return representation


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    products = OrderItemsSerializer(many=True)

    class Meta:
        model = Order
        fields = ['user', 'country', 'country_id', 'products']
    
    def create(self, validated_data):
        products_data = validated_data.pop('products')
        order = Order.objects.create(**validated_data)
        order_products = [OrderItem(order=order, **fields) for fields in products_data]
        OrderItem.objects.bulk_create(order_products)
        return order
    
    def update(self, instance, validated_data):
        products_data = validated_data.pop('products', None)
        order_products = OrderItem.objects.filter(order=instance)

        instance.country = validated_data.get('country', instance.country)
        instance.country_id = validated_data.get('country_id', instance.country_id)
        instance.save()

        if products_data:
            order_products.delete()
            order_products = [OrderItem(order=instance, **fields) for fields in products_data]
            OrderItem.objects.bulk_create(order_products)

        return instance


class ProductSerializer(serializers.ModelSerializer):
    sales_price = serializers.DecimalField(max_digits=8, decimal_places=2, source='price')
    discount_price = serializers.DecimalField(max_digits=8, decimal_places=2, source='get_discount_price')

    class Meta:
        model = Product
        fields = ['title', 'sales_price', 'discount_price']
