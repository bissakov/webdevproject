from rest_framework import serializers
from store.models import Consumer,Category,Product,Order,OrderProduct

class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'phone', 'address')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'price', 'category', 'likes')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('consumer', 'created_at', 'updated_at')

class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('product', 'order', 'amount')
