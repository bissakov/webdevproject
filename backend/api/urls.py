from django.contrib import admin
from django.shortcuts import render, redirect
from django.urls import path, include, re_path
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

def home(request):
    return render(request, 'store/index.html')

def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()

    return render(request, 'store/login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('/')
    else:
        form = UserCreationForm()

    context = {'form' : form}
    return render(request, 'store/signup.html', context)

def logout_view(request):
    logout(request)
    home()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('home', home),
    path('api/', include('store.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signin/', signin, name='login'),
    path('accounts/signup/', signup, name='signup'),
    path('accounts/logout/', logout_view, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += [
#     re_path(r'(?P<path>.*)', FrontendRenderView.as_view(), name='home')
# ]