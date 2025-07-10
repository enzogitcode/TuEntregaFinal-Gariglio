from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from ..models import Teacher
from django.urls import reverse_lazy

from django.shortcuts import render

def TeachersHome(request):
    return render(request, 'AppBlog/teachers/teachers_home.html')

class TeacherListView(ListView):
    model = Teacher
    template_name = 'AppBlog/teachers/teachers_list.html'
    
class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'AppBlog/teachers/teacher_detail.html'

class TeacherCreateView(CreateView):
    model = Teacher
    fields = ['name', 'last_name', 'age', 'course', 'college', 'email']
    template_name = 'AppBlog/teachers/create_teacher_form.html'
    success_url = reverse_lazy('teachers_list')

class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = ['name', 'last_name', 'age', 'course', 'college', 'email']
    template_name = 'AppBlog/teachers/teachers_update_form.html'
    success_url = reverse_lazy('teachers_list')

class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'AppBlog/teachers/teachers_delete_form.html'
    success_url = reverse_lazy('home')  

