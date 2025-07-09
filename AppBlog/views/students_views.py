from django.views.generic import ListView # Importamos ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from ..models import Student


def student():
    pass

class StudentListView(ListView):
    model= Student
    template_name= 'AppBlog/students/students_list.html'

class StudentCreateView(CreateView):
    model= Student
    fields= ['name']
    template_name= 'AppBlog/students/create_students_form.html'
    success_url= 'students_list'

class StudentUpdateView(UpdateView):
    model= Student
    fields= ['name']
    template_name= 'AppBlog/students/students_update_form.html'
    success_url= 'student_detail'

class StudentDeleteView(DeleteView):
    model= Student
    template_name= 'AppBlog/students/students_delete_form.html'
    success_url= 'app/home.html'
    