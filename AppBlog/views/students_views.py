from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from AppBlog.models import Student
from AppBlog.forms import StudentRegisterForm

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
