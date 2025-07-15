from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TeacherRegisterForm(UserCreationForm):
    course = forms.CharField(max_length=100)
    college = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'course', 'college']

class StudentRegisterForm(UserCreationForm):
    career = forms.CharField(max_length=100)
    college = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'career', 'college']

class BasicUserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
