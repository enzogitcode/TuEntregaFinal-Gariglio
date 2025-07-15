from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from ..models import Student
from django.urls import reverse_lazy
from django.shortcuts import render

def StudentsHome(request):
    return render(request, 'AppBlog/students/students_home.html')

def students_search(request):
    return render(request, 'AppBlog/students/students_search.html')

def students_results(request):
    keyword = request.GET.get('keyword') 
    filtro = request.GET.get('filtro')   

    students = Student.objects.all()

    if keyword and filtro:
        if filtro == 'name':
            students = students.filter(name__icontains=keyword)
        elif filtro == 'last_name':
            students = students.filter(last_name__icontains=keyword)
        elif filtro == 'course':
            students = students.filter(course__icontains=keyword)
        elif filtro == 'career':
            students = students.filter(career__icontains=keyword)
        elif filtro == 'email':
            students = students.filter(email__icontains=keyword)
        elif filtro == 'age':
            students = students.filter(age__icontains=keyword)

    context = {
        'students': students,
        'keyword': keyword,
        'filtro': filtro,
    }
    return render(request, 'AppBlog/students/students_results.html', context)


class StudentListView(ListView):
    model = Student
    template_name = 'AppBlog/students/students_list.html'
    context_object_name= 'students'
    ordering= ['last_name']

class StudentDetailView(DetailView):
    model = Student
    template_name = 'AppBlog/students/student_detail.html'

class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'last_name', 'age', 'career', 'college', 'email']
    template_name = 'AppBlog/students/create_student_form.html'
    success_url = reverse_lazy('students_list')
    def test_func(self):
        return self.request.user.is_superuser

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'last_name', 'age', 'career', 'college', 'email']
    template_name = 'AppBlog/students/student_update_form.html'
    success_url = reverse_lazy('students_list')  

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'AppBlog/students/student_delete_form.html'
    success_url = reverse_lazy('students_list')
