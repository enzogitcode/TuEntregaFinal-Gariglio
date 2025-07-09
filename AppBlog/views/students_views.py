from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from ..models import Student
from django.urls import reverse_lazy

class StudentListView(ListView):
    model = Student
    template_name = 'AppBlog/students/students_list.html'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'AppBlog/students/student_detail.html'

class StudentCreateView(CreateView):
    model = Student
    fields = ['name']
    template_name = 'AppBlog/students/create_student_form.html'
    success_url = reverse_lazy('students_list')

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name']
    template_name = 'AppBlog/students/students_update_form.html'
    success_url = reverse_lazy('students_list')  # O 'student_detail' si tenés esa vista

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'AppBlog/students/students_delete_form.html'
    success_url = reverse_lazy('home')  # Asumiendo que 'home' es tu vista de inicio
