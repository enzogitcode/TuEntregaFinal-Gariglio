from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from ..forms import BasicUserRegisterForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from AppBlog.models import Avatar

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

@login_required
def home_user(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, 'AppBlog/home.html', {"url": avatares[0].imagen.url})

from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from ..models import CustomUser
from ..forms import AvatarUploadForm

class AvatarUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = AvatarUploadForm
    template_name = 'AppBlog/user/avatar_edit.html'
    success_url = reverse_lazy('home_user')

    def get_object(self):
        return self.request.user
