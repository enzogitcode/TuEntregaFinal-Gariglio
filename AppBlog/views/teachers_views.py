from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from ..models import Teacher
from django.urls import reverse_lazy


from django.shortcuts import render

def teachers_home(request):
    return render(request, 'AppBlog/teachers/teachers_home.html')

def teachers_search(request):
    return render(request, 'AppBlog/teachers/teachers_search.html')

def teachers_results(request):
    keyword = request.GET.get('keyword') 
    filtro = request.GET.get('filtro')   

    teachers = Teacher.objects.all()

    if keyword and filtro:
        if filtro == 'name':
            teachers = teachers.filter(name__icontains=keyword)
        elif filtro == 'last_name':
            teachers = teachers.filter(last_name__icontains=keyword)
        elif filtro == 'course':
            teachers = teachers.filter(course__icontains=keyword)
        elif filtro == 'college':
            teachers = teachers.filter(college__icontains=keyword)
        elif filtro == 'email':
            teachers = teachers.filter(email__icontains=keyword)
        elif filtro == 'age':
            teachers = teachers.filter(age__icontains=keyword)

    context = {
        'teachers': teachers,
        'keyword': keyword,
        'filtro': filtro,
    }
    return render(request, 'AppBlog/teachers/teachers_results.html', context)

class TeacherListView(ListView):
    model = Teacher
    template_name = 'AppBlog/teachers/teachers_list.html'
    context_object_name= 'teachers'
    
class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'AppBlog/teachers/teacher_detail.html'

class TeacherCreateView(CreateView):
    model = Teacher
    fields = ['name', 'last_name', 'age', 'course', 'college', 'email']
    template_name = 'AppBlog/teachers/create_teacher_form.html'
    success_url = reverse_lazy('teachers_list')
    context_object_name= 'teachers'

class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = ['name', 'last_name', 'age', 'course', 'college', 'email']
    template_name = 'AppBlog/teachers/teacher_update_form.html'
    success_url = reverse_lazy('teachers_list')
    context_object_name= 'teachers'

class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'AppBlog/teachers/teacher_delete_form.html'
    success_url = reverse_lazy('teachers_list')  
    context_object_name= 'teachers'

class TeacherSearchView(ListView):
    model = Teacher
    template_name = 'AppBlog/teachers/results_template.html'
    context_object_name = 'teachers'

        
    