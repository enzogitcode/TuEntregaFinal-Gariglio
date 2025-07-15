from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from ..models import Student, Teacher
from ..forms import TeacherRegisterForm, StudentRegisterForm, BasicUserRegisterForm
from django.shortcuts import render

def register_choose_your_role(request):
    return render(request, 'AppBlog/user/register_choose_your_role.html')

class TeacherRegisterView(CreateView):
    form_class = TeacherRegisterForm
    template_name = 'AppBlog/user/register_teacher.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        Teacher.objects.create(
            user=user,
            course=form.cleaned_data['course'],
            college=form.cleaned_data['college']
        )
        return super().form_valid(form)

class StudentRegisterView(CreateView):
    form_class = StudentRegisterForm
    template_name = 'AppBlog/user/register_student.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        Student.objects.create(
            user=user,
            career=form.cleaned_data['career'],
            college=form.cleaned_data['college']
        )
        return super().form_valid(form)

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
