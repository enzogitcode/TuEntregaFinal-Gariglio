from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import render

def teachers_home(request):
    return render(request, 'AppBlog/teachers/teachers_home.html')

from AppBlog.models import Teacher
from AppBlog.forms.TeachersForms import TeacherRegisterForm, TeacherSelfEditForm

class TeacherRegisterView(CreateView):
    form_class = TeacherRegisterForm
    template_name = 'AppBlog/user/register_form.html'
    success_url = reverse_lazy('users:login')
    extra_context = { 'tipo': 'Docente' }

class TeacherSelfUpdateView(LoginRequiredMixin, UpdateView):
    model = Teacher
    form_class = TeacherSelfEditForm
    template_name = 'AppBlog/teachers/teacher_update_form.html'
    success_url = reverse_lazy('teachers:list')

    def get_object(self):
        return Teacher.objects.get(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user_instance'] = self.request.user
        return kwargs

class TeacherListView(ListView):
    model = Teacher
    template_name = 'AppBlog/shared/list.html'
    context_object_name = 'items'
    extra_context = {
        'tipo': 'Docentes',
        'detail_url': 'teachers:detail',
        'create_url': None,
        'show_create_button': False
    }


class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'AppBlog/shared/detail.html'
    context_object_name = 'obj'
    extra_context = {
        'tipo': 'Docente'
    }

class TeacherSearchView(ListView):
    model = Teacher
    template_name = 'AppBlog/shared/search.html'
    context_object_name = 'items'

    def get_queryset(self):
        query = self.request.GET.get('q', '').strip()
        if query:
            return Teacher.objects.filter(
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query) |
                Q(course__icontains=query) |
                Q(college__icontains=query)
            ).distinct()
        return Teacher.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        context['tipo'] = 'Docente'
        context['detail_url'] = 'teachers:detail'
        return context
