from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from store.models import Consumer,Category,Product,Order,OrderProduct
from serializers import ConsumerSerializer,CategorySerializer,ProductSerializer,OrderSerializer,OrderProductSerializer

class ConsumerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ConsumerSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = OrderSerializer

class OrderProductViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = OrderProductSerializer