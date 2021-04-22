from rest_framework import serializers
from store.models import Product

class ExampleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price')