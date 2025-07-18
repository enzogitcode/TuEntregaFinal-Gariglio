# 📦 Django base
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, ListView, DetailView

# 👤 Modelos propios
from ..models import CustomUser, Teacher, Student, Avatar, Paper, Article

# 📝 Formularios
from ..forms.UsersForms import (
    BasicUserRegisterForm,
    BasicUserSelfEditForm,
    AvatarUploadForm,
    TeacherSelfEditForm,
    StudentSelfEditForm
)


def register_choose_your_role(request):
    return render(request, 'AppBlog/user/register_choose_your_role.html')

class UserRegisterView(CreateView):
    form_class = BasicUserRegisterForm
    template_name = 'AppBlog/user/register_user.html'
    success_url = reverse_lazy('users:login')
    extra_context = { 'tipo': 'Usuario Común' }

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'AppBlog/user/login.html'

class Logout(LogoutView):
    next_page = 'users:login'

@login_required
def home_user(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, 'AppBlog/users/user_home.html', {"url": avatares[0].imagen.url})

@login_required
def profile(request):
    user = request.user
    articles = Article.objects.filter(author=user)
    papers = Paper.objects.filter(author=user)

    context = {
        'user': user,
        'articles': articles,
        'papers': papers
    }
    return render(request, 'AppBlog/user/profile.html', context)


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = 'AppBlog/user/profile_edit.html'
    success_url = reverse_lazy('users:profile')
    form_class = BasicUserSelfEditForm

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
    
from django.http import HttpResponseForbidden

@login_required
def users_list(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Acceso restringido.")
    users = CustomUser.objects.all().order_by('username')
    return render(request, 'AppBlog/user/users_list.html', {'users': users})


@login_required
def user_dashboard(request):
    user = request.user
    avatar_obj = Avatar.objects.filter(user=user).first()

    context = {
        'user': user,
        'avatar_url': avatar_obj.imagen.url if avatar_obj and avatar_obj.imagen else None
    }
    return render(request, 'AppBlog/user/user_home.html', context)

class AvatarUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = AvatarUploadForm
    template_name = 'AppBlog/user/update_avatar.html'
    success_url = reverse_lazy('users:profile') 

    def get_object(self):
        return self.request.user
