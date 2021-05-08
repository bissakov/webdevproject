from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from django.http import JsonResponse,HttpResponse
from store.models import Consumer,Category,Product,Order,OrderProduct
from store.serializers import ConsumerModelSerializer,CategoryModelSerializer,ProductModelSerializer,OrderModelSerializer,OrderProductModelSerializer

from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from django.core import serializers

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Product-list': '/product-list',
        'Product-detail': '/product-list/<str:pk>/',
        'Category-list': '/category-list',
    }
    return Response(api_urls)

class ProductViewSet(APIView):
    def get(self,request,format=None):
        queryset = Product.objects.all()
        serializer = ProductModelSerializer(queryset, many=True)
        return Response(serializer.data)

class ProductDetailViewSet(APIView):
    def get(self,request,pk,format=None):
        queryset = Product.objects.get(id=pk)
        serializer = ProductModelSerializer(queryset, many=False)
        return Response(serializer.data)

@api_view(['GET'])
def categoryViewSet(request):
    queryset = Category.objects.all()
    serializer = CategoryModelSerializer(queryset, many=True)
    return Response(serializer.data)