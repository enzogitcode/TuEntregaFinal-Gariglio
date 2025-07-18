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
    success_url = reverse_lazy('teachers:list')
    extra_context = { 'tipo': 'Docente' }
    # No necesitas form_valid, el form ya crea Teacher y Profile

class TeacherSelfUpdateView(LoginRequiredMixin, UpdateView):
    model = Teacher
    form_class = TeacherSelfEditForm
    template_name = 'AppBlog/teachers/teacher_update_form.html'
    success_url = reverse_lazy('teachers_list')

    def get_object(self):
        return Teacher.objects.get(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user_instance'] = self.request.user
        return kwargs

class TeacherListView(ListView):
    model = Teacher
    template_name = 'AppBlog/teachers/teachers_list.html'
    context_object_name = 'teachers'

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'AppBlog/teachers/teacher_detail.html'
    context_object_name = 'teacher'

class TeacherDeleteView(UserPassesTestMixin, DeleteView):
    model = Teacher
    template_name = 'AppBlog/teachers/confirm_delete.html'
    success_url = reverse_lazy('teachers_list')
    context_object_name = 'teacher'

    def test_func(self):
        return self.request.user.is_superuser

class TeacherSearchView(ListView):
    model = Teacher
    template_name = 'AppBlog/teachers/teachers_search.html'
    context_object_name = 'teachers'

    def get_queryset(self):
        query = self.request.GET.get('q', '').strip()  

        if query:
            return Teacher.objects.filter(
                Q(user__first_name__icontains=query) |  
                Q(user__last_name__icontains=query) |   
                Q(college__icontains=query) |           
                Q(course__icontains=query)              
            ).distinct()  

        return Teacher.objects.all()  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')  
        return context