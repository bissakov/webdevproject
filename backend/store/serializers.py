from rest_framework import serializers
from store.models import Consumer,Category,Product,Order,OrderProduct

# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(required=True, allow_blank=True, max_length=250)
#     description = serializers.CharField(required=True, allow_blank=True, max_length=500)
#     price = serializers.IntegerField(read_only=True)
#     category = serializers.CharField(required=True, allow_blank=True, max_length=250)
#     likes = serializers.IntegerField(read_only=True)


#     def create(self, validated_data):
#         return Product.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.id = validated_data.get('id', instance.id)
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.price = validated_data.get('price', instance.price)
#         instance.category = validated_data.get('category', instance.category)
#         instance.likes = validated_data.get('likes', instance.likes)
#         instance.save()
#         return instance

class ConsumerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'phone', 'address')

class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name',)

class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'price', 'category', 'likes')

class OrderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('consumer', 'created_at', 'updated_at')

class OrderProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('product', 'order', 'amount')
