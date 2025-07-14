from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserChangeForm
from django.views.generic.edit import UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django import forms

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'AppBlog/user/register.html'
    success_url = reverse_lazy('login')

class UserEditForm(UserCreationForm):
    email= forms.EmailField(label='Modificar el e-mail')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()
    class Meta:
        #model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']

class EditUserView(LoginRequiredMixin, UpdateView):
    form_class = UserChangeForm
    template_name = 'AppBlog/user/edit.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user

class CustomLoginView(LoginView):
    template_name = 'AppBlog/user/login.html'

class Logout(LogoutView):
    next_page = 'login'
