from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import User
from AppBlog.models import Teacher

# Teachers
# registro del profesor
class TeacherRegisterForm(UserCreationForm):
    course = forms.CharField(max_length=100)
    college = forms.CharField(max_length=100)
    age = forms.IntegerField(required=False)

    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2',
            'first_name', 'last_name'
        ]

# registro para autoeditarse
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
    
class TeacherSelfUpdateView(LoginRequiredMixin, UpdateView):
    model = Teacher
    form_class = TeacherSelfEditForm
    template_name = 'AppBlog/teachers/update_self.html'
    success_url = reverse_lazy('teachers_list')  # o donde quieras redirigir

    def get_object(self):
        return Teacher.objects.get(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user_instance'] = self.request.user
        return kwargs



# Students

class StudentRegisterForm(UserCreationForm):
    career = forms.CharField(max_length=100)
    college = forms.CharField(max_length=100)
    age= forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'career', 'college']

class BasicUserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
