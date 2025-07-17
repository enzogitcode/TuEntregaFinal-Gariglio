from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from ..forms import (
    BasicUserSelfEditForm, TeacherSelfEditForm, StudentSelfEditForm, AvatarUploadForm, BasicUserRegisterForm
)
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import CustomUser, Teacher, Student, Avatar
from django.views.generic import ListView, UpdateView, CreateView, DetailView

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


class AvatarUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = AvatarUploadForm
    template_name = 'AppBlog/user/avatar_edit.html'
    success_url = reverse_lazy('home_user')

    def get_object(self):
        return self.request.user


class ProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'AppBlog/user/profile.html'
    context_object_name = 'user'

    def get_object(self):
        return get_object_or_404(CustomUser, pk=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        role = self.request.user.role

        if role == 'teacher':
            context['teacher'] = Teacher.objects.filter(user=self.request.user).first()
        elif role == 'student':
            context['student'] = Student.objects.filter(user=self.request.user).first()

        return context


@login_required
def profile(request):
    return render(request, 'AppBlog/user/profile.html', {'user': request.user})


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = 'AppBlog/user/profile_edit.html'
    success_url = reverse_lazy('profile')
    form_class = BasicUserSelfEditForm  # default

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Extra formularios según rol
        role = self.request.user.role

        if role == 'teacher':
            teacher = Teacher.objects.filter(user=self.request.user).first()
            context['extra_form'] = TeacherSelfEditForm(instance=teacher)
        elif role == 'student':
            student = Student.objects.filter(user=self.request.user).first()
            context['extra_form'] = StudentSelfEditForm(instance=student)
        context['avatar_form'] = AvatarUploadForm(instance=self.request.user)

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        basic_form = BasicUserSelfEditForm(request.POST, instance=self.object)
        avatar_form = AvatarUploadForm(request.POST, request.FILES, instance=self.object)

        role = request.user.role
        extra_form = None

        if role == 'teacher':
            teacher = Teacher.objects.filter(user=request.user).first()
            extra_form = TeacherSelfEditForm(request.POST, instance=teacher)
        elif role == 'student':
            student = Student.objects.filter(user=request.user).first()
            extra_form = StudentSelfEditForm(request.POST, instance=student)

        if basic_form.is_valid() and avatar_form.is_valid() and (extra_form is None or extra_form.is_valid()):
            basic_form.save()
            avatar_form.save()
            if extra_form:
                extra_form.save()
            return redirect(self.success_url)

        context = self.get_context_data()
        context['form'] = basic_form
        context['avatar_form'] = avatar_form
        context['extra_form'] = extra_form
        return self.render_to_response(context)
    
class UsersListView(ListView):
    model = CustomUser
    template_name= 'AppBlog/user/users_list.html'
    context_object_name= 'users'
