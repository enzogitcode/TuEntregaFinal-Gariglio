from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from ..forms import BasicUserRegisterForm
from django.shortcuts import render

def register_choose_your_role(request):
    return render(request, 'AppBlog/user/register_choose_your_role.html')

class UserRegisterView(CreateView):
    form_class = BasicUserRegisterForm
    template_name = 'AppBlog/user/register_user.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'AppBlog/user/login.html'

class Logout(LogoutView):
    next_page = 'login'
