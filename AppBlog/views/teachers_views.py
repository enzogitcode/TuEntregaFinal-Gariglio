from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from AppBlog.models import Teacher
from AppBlog.forms import TeacherRegisterForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from AppBlog.forms import TeacherSelfEditForm
from django.views.generic import ListView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Q
from AppBlog.forms import TeacherSearchForm
from django.shortcuts import render

def teachers_home(request):
    return render ('AppBlog/teachers/teachers_home.html')

# registrarse como profesor/docente

class TeacherRegisterView(CreateView):
    form_class = TeacherRegisterForm
    template_name = 'AppBlog/user/register_teacher.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        Teacher.objects.create(
            user=user,
            course=form.cleaned_data['course'],
            college=form.cleaned_data['college'],
            age=form.cleaned_data['age']
        )
        return super().form_valid(form)

# editar

class TeacherSelfUpdateView(LoginRequiredMixin, UpdateView):
    model = Teacher
    form_class = TeacherSelfEditForm
    template_name = 'AppBlog/teachers/update_self.html'
    success_url = reverse_lazy('teachers_list')

    def get_object(self):
        return Teacher.objects.get(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user_instance'] = self.request.user
        return kwargs

# listar todos los profesores

class TeacherListView(ListView):
    model = Teacher
    template_name = 'AppBlog/teachers/teacher_list.html'
    context_object_name = 'teachers'

# detalles de un profesor en particular

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'AppBlog/teachers/teacher_detail.html'
    context_object_name = 'teacher'


# Vista para que el SUPERUSUARIO pueda eliminar un docente en particular

class TeacherDeleteView(UserPassesTestMixin, DeleteView):
    model = Teacher
    template_name = 'AppBlog/teachers/confirm_delete.html'
    success_url = reverse_lazy('teachers_list')
    context_object_name = 'teacher'

    def test_func(self):
        return self.request.user.is_superuser


class TeacherSearchView(ListView):
    model = Teacher
    template_name = 'AppBlog/teachers/teacher_search.html'
    context_object_name = 'teachers'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name', '')
        last_name = self.request.GET.get('last_name', '')
        college = self.request.GET.get('college', '')
        course = self.request.GET.get('course', '')

        if name or last_name or college or course:
            queryset = queryset.filter(
                Q(user__first_name__icontains=name) &
                Q(user__last_name__icontains=last_name) &
                Q(college__icontains=college) &
                Q(course__icontains=course)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TeacherSearchForm(self.request.GET)
        return context
