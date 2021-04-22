from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include, re_path
from django.http import HttpResponse

def home(request):
    return render(request, 'store/front-end-render.html')

def about(request):
    return HttpResponse('About')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('about/', about)
    #path('login',Auth.as_view())
]

# urlpatterns += [
#     re_path(r'(?P<path>.*)', FrontendRenderView.as_view(), name='home')
# ]