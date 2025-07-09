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
    success_url = 'teachers_list'

class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = ['name', 'last_name', 'age', 'course', 'college', 'email']
    template_name = 'AppBlog/teachers/teachers_update_form.html'
    success_url = 'teacher_detail'

class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'AppBlog/teachers/teachers_delete_form.html'
    success_url = 'app/home.html'  