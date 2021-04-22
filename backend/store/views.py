from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'store/front-end-render.html')

def products(request):
    return HttpResponse('products')

def customer(request):
    return HttpResponse('customer')
