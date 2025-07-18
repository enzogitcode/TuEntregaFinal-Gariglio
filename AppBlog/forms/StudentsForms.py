from django import forms
from django.contrib.auth.forms import UserCreationForm
from ..models import CustomUser, Student
from django.core.exceptions import ValidationError

# 🔸 Registro: Student
class StudentRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    career = forms.CharField(label='Carrera', required=True)
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
        user.role = 'student'
        if commit:
            user.save()
            Student.objects.create(
                user=user,
                career=self.cleaned_data['career'],
                college=self.cleaned_data['college'],
                age=self.cleaned_data['age'],
            )
        return user

# edición

class StudentSelfEditForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['career', 'college', 'age']

# 🔸 Búsqueda: Teacher
class StudentSearchForm(forms.Form):
    name = forms.CharField(label='Nombre', required=False)
    last_name = forms.CharField(label='Apellido', required=False)
    career = forms.CharField(label='Carrera', required=False)
    college = forms.CharField(label='Institución', required=False)