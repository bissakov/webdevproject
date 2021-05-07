from rest_framework import serializers
from store.models import Consumer,Category,Product,Order,OrderProduct

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

# class RegistrationModelSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
#     class Meta:
#         model = Account
#         fields = ['email', 'username', 'password', 'password2']
#         extra_kwarg = {
#             'password': {'write_only': True}
#         }

#     def save(self):
#         account = Account(
#             email = self.validated_data['email'].
#             username = self.validated_data['username'],
#         )
#         password = self.validated_data['password']
#         password2 = self.validated_data['password2']
#         if password != password2:
#             raise serializers.ValidationError({'password': 'Passwords must match.'})
#         account.set_password(password)
#         account.save()