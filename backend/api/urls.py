from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include, re_path
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

def home(request):
    return render(request, 'store/index.html')

def about(request):
    return HttpResponse('About')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('about/', about),
    #path('login',Auth.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += [
#     re_path(r'(?P<path>.*)', FrontendRenderView.as_view(), name='home')
# ]