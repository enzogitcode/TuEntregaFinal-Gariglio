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
from AppBlog.forms import TeacherRegisterForm, TeacherSelfEditForm, TeacherSearchForm

class TeacherRegisterView(CreateView):
    form_class = TeacherRegisterForm
    template_name = 'AppBlog/user/register_teacher.html'
    success_url = reverse_lazy('login')
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
        queryset = super().get_queryset()
        name = self.request.GET.get('name', '')
        last_name = self.request.GET.get('last_name', '')
        college = self.request.GET.get('college', '')
        course = self.request.GET.get('course', '')

        filters = Q()
        if name:
            filters &= Q(user__first_name__icontains=name)
        if last_name:
            filters &= Q(user__last_name__icontains=last_name)
        if college:
            filters &= Q(college__icontains=college)
        if course:
            filters &= Q(course__icontains=course)

        return queryset.filter(filters)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TeacherSearchForm(self.request.GET)
        return context