from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.db.models import Q
from AppBlog.models import Student
from AppBlog.forms.StudentsForms import StudentRegisterForm, StudentSelfEditForm

def students_home(request):
    return render (request, 'AppBlog/students/students_home.html')

#1. Registro de estudiante
class StudentRegisterView(CreateView):
    form_class = StudentRegisterForm
    template_name = 'AppBlog/user/register_form.html'
    success_url = reverse_lazy('users:login')
    extra_context = { 'tipo': 'Estudiante' }
    
#2. Edición de perfil propio
class StudentSelfUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentSelfEditForm
    template_name = 'AppBlog/students/update_self.html'
    success_url = reverse_lazy('students:list')

    def get_object(self):
        return Student.objects.get(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user_instance'] = self.request.user
        return kwargs

class StudentListView(ListView):
    model = Student
    template_name = 'AppBlog/shared/list.html'
    context_object_name = 'items'
    extra_context = {
        'tipo': 'Estudiantes',
        'detail_url': 'students:detail',
        'create_url': None,
        'show_create_button': False
    }



class StudentDetailView(DetailView):
    model = Student
    template_name = 'AppBlog/shared/detail.html'
    context_object_name = 'obj'
    extra_context = {
        'tipo': 'Estudiante'
    }

class StudentDeleteView(UserPassesTestMixin, DeleteView):
    model = Student
    template_name = 'AppBlog/students/confirm_delete.html'
    context_object_name = 'obj'  
    success_url = reverse_lazy('students_list')

    def test_func(self):
        return self.request.user.is_superuser

class StudentSearchView(ListView):
    model = Student
    template_name = 'AppBlog/shared/search.html'
    context_object_name = 'items'

    def get_queryset(self):
        query = self.request.GET.get('q', '').strip()
        if query:
            return Student.objects.filter(
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query) |
                Q(career__icontains=query) |
                Q(college__icontains=query)
            ).distinct()
        return Student.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        context['tipo'] = 'Estudiante'
        context['detail_url'] = 'students:detail'
        return context

