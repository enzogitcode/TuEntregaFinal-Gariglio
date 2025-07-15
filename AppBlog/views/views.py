from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from AppBlog.models import Avatar

@login_required
def home(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, 'AppBlog/home.html', {"url": avatares[0].imagen.url})

def about(request):
    return render(request, 'AppBlog/about.html')



