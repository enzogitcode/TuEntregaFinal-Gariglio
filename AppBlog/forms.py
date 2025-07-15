from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppBlog.models import Teacher
from django import forms

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


class TeacherSearchForm(forms.Form):
    name = forms.CharField(label='Nombre', required=False)
    last_name = forms.CharField(label='Apellido', required=False)
    college = forms.CharField(label='Institución', required=False)
    course = forms.CharField(label='Curso', required=False)


## Students Forms

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StudentRegisterForm(UserCreationForm):
    career = forms.CharField(max_length=100)
    college = forms.CharField(max_length=100)
    age = forms.IntegerField(required=False)

    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2',
            'first_name', 'last_name'
        ]

from AppBlog.models import Student

class StudentSelfEditForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()

    class Meta:
        model = Student
        fields = ['career', 'college', 'age']

    def __init__(self, *args, **kwargs):
        self.user_instance = kwargs.pop('user_instance', None)
        super().__init__(*args, **kwargs)

        if self.user_instance:
            self.fields['first_name'].initial = self.user_instance.first_name
            self.fields['last_name'].initial = self.user_instance.last_name
            self.fields['email'].initial = self.user_instance.email

    def save(self, commit=True):
        student = super().save(commit=False)
        if self.user_instance:
            self.user_instance.first_name = self.cleaned_data['first_name']
            self.user_instance.last_name = self.cleaned_data['last_name']
            self.user_instance.email = self.cleaned_data['email']
            if commit:
                self.user_instance.save()
        if commit:
            student.save()
        return student

class StudentSearchForm(forms.Form):
    name = forms.CharField(label='Nombre', required=False)
    last_name = forms.CharField(label='Apellido', required=False)
    college = forms.CharField(label='Institución', required=False)
    career = forms.CharField(label='Carrera', required=False)


## usuarios comunesclass BasicUserRegisterForm(UserCreationForm):
class BasicUserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
