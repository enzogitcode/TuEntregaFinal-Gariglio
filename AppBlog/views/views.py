from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from AppBlog.models import Avatar

def home(request):
    return render(request, 'AppBlog/home.html')

def about(request):
    return render(request, 'AppBlog/about.html')

def forbidden(request):
    return render(request, 'AppBlog/forbidden.html')


