from django.shortcuts import render


from .models import models

def home(request):
    return render(request, 'AppBlog/home.html')
