from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from AppBlog.models import Student
from AppBlog.forms import StudentRegisterForm
from django.shortcuts import render

def students_home(request):
    return render (request, 'AppBlog/students/students_home.html')

#1. Registro de estudiante
class StudentRegisterView(CreateView):
    form_class = StudentRegisterForm
    template_name = 'AppBlog/user/register_student.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        Student.objects.create(
            user=user,
            career=form.cleaned_data['career'],
            college=form.cleaned_data['college'],
            age=form.cleaned_data['age']
        )
        return super().form_valid(form)
    
#2. Edición de perfil propio
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from AppBlog.models import Student
from AppBlog.forms import StudentSelfEditForm

class StudentSelfUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentSelfEditForm
    template_name = 'AppBlog/students/update_self.html'
    success_url = reverse_lazy('students_list')

    def get_object(self):
        return Student.objects.get(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user_instance'] = self.request.user
        return kwargs

from django.views.generic import ListView
from AppBlog.models import Student

class StudentListView(ListView):
    model = Student
    template_name = 'AppBlog/students/students_list.html'
    context_object_name = 'students'

from django.views.generic.detail import DetailView
from AppBlog.models import Student

class StudentDetailView(DetailView):
    model = Student
    template_name = 'AppBlog/students/student_detail.html'
    context_object_name = 'student'

from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin

class StudentDeleteView(UserPassesTestMixin, DeleteView):
    model = Student
    template_name = 'AppBlog/students/confirm_delete.html'
    success_url = reverse_lazy('students_list')
    context_object_name = 'student'

    def test_func(self):
        return self.request.user.is_superuser

from django.db.models import Q
from AppBlog.forms import StudentSearchForm

class StudentSearchView(ListView):
    model = Student
    template_name = 'AppBlog/students/students_search.html'
    context_object_name = 'students'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name', '')
        last_name = self.request.GET.get('last_name', '')
        college = self.request.GET.get('college', '')
        career = self.request.GET.get('career', '')

        filters = Q()
        if name:
            filters &= Q(user__first_name__icontains=name)
        if last_name:
            filters &= Q(user__last_name__icontains=last_name)
        if college:
            filters &= Q(college__icontains=college)
        if career:
            filters &= Q(career__icontains=career)

        return queryset.filter(filters)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = StudentSearchForm(self.request.GET)
        return context
