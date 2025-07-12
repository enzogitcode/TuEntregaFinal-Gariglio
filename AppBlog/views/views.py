from django.shortcuts import render

def home(request):
    return render(request, 'AppBlog/home.html')

def about(request):
    return render(request, 'AppBlog/about.html')


