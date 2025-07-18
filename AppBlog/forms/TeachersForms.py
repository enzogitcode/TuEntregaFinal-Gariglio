from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from ..models import CustomUser, Teacher

# 🔸 Registro: Teacher

class TeacherRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    course = forms.CharField(label='Materia', required=True)
    college = forms.CharField(label='Institución', required=True)
    age = forms.IntegerField(label='Edad', required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Este correo ya está registrado.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'teacher'
        if commit:
            user.save()
            Teacher.objects.create(
                user=user,
                course=self.cleaned_data['course'],
                college=self.cleaned_data['college'],
                age=self.cleaned_data['age'],
            )
        return user

# 🔸 Autoedición: Teacher
class TeacherSelfEditForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['course', 'college', 'age']

