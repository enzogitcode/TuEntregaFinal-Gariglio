from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from ..models import Teacher
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from AppBlog.models import Teacher
from AppBlog.forms import TeacherSelfEditForm, TeacherRegisterForm
from django.shortcuts import render

class TeacherRegisterView(CreateView):
    form_class = TeacherRegisterForm
    template_name = 'AppBlog/user/register_teacher.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        Teacher.objects.create(
            user=user,
            course=form.cleaned_data['course'],
            college=form.cleaned_data['college'],
            age=form.cleaned_data['age']
        )
        print(form.cleaned_data['age'])
        return super().form_valid(form)

class TeacherSelfEditForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()

    class Meta:
        model = Teacher
        fields = ['course', 'college', 'age']

    def __init__(self, *args, **kwargs):
        self.user_instance = kwargs.pop('user_instance', None)
        super().__init__(*args, **kwargs)

        if self.user_instance:
            self.fields['first_name'].initial = self.user_instance.first_name
            self.fields['last_name'].initial = self.user_instance.last_name
            self.fields['email'].initial = self.user_instance.email

    def save(self, commit=True):
        teacher = super().save(commit=False)

        if self.user_instance:
            self.user_instance.first_name = self.cleaned_data['first_name']
            self.user_instance.last_name = self.cleaned_data['last_name']
            self.user_instance.email = self.cleaned_data['email']
            if commit:
                self.user_instance.save()

        if commit:
            teacher.save()

        return teacher
















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
    
class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'AppBlog/teachers/teacher_delete_form.html'
    success_url = reverse_lazy('teachers_list')  
    context_object_name= 'teachers'

class TeacherSearchView(ListView):
    model = Teacher
    template_name = 'AppBlog/teachers/results_template.html'
    context_object_name = 'teachers'

        
    