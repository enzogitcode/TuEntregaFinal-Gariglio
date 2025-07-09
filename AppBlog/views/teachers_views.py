from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from ..models import Teacher

class TeacherListView(ListView):
    model = Teacher
    template_name = 'AppBlog/teachers/teachers_list.html'

class TeacherCreateView(CreateView):
    model = Teacher
    fields = ['name', 'last_name', 'age', 'course', 'college', 'email']
    template_name = 'AppBlog/teachers/create_teacher_form.html'
    success_url = 'teachers_list'  # Asegúrate de tener esta URL nombrada en tu urls.py

class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = ['name', 'last_name', 'age', 'course', 'college', 'email']
    template_name = 'AppBlog/teachers/teachers_update_form.html'
    success_url = 'teacher_detail'  # Asegúrate de tener esta URL nombrada en tu urls.py

class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'AppBlog/teachers/teachers_delete_form.html'
    success_url = 'app/home.html'  # O usa reverse_lazy si es una URL nombrada

# Si estás usando success_url con nombres de URL, considera usar reverse_lazy para evitar errores de importación circular:

# python
# from django.urls import reverse_lazy

# success_url = reverse_lazy('teachers_list')
# Asegúrate de tener las plantillas correspondientes en las rutas indicadas:

# AppBlog/teachers/teachers_list.html

# AppBlog/teachers/create_teacher_form.html

# AppBlog/teachers/teachers_update_form.html

# AppBlog/teachers/teachers_delete_form.html