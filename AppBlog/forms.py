
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .models import Student, Teacher, CustomUser

# 🔸 Registro: usuario común
class BasicUserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

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
        user.role = 'user'
        if commit:
            user.save()
        return user

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

# 🔸 Autoedición: Teacher
class TeacherSelfEditForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['course', 'college', 'age']

# 🔸 Autoedición: Student
class StudentSelfEditForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['career', 'college', 'age']

# 🔸 Autoedición: usuario base
class BasicUserSelfEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        email = self.cleaned_data['email']
        user_id = self.instance.id
        if CustomUser.objects.filter(email=email).exclude(id=user_id).exists():
            raise ValidationError("Este correo ya está en uso por otro usuario.")
        return email

# 🔸 Subida de avatar
class AvatarUploadForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['avatar']

# 🔸 Búsqueda: Teacher
class TeacherSearchForm(forms.Form):
    name = forms.CharField(label='Nombre', required=False)
    last_name = forms.CharField(label='Apellido', required=False)
    course = forms.CharField(label='Materia', required=False)
    college = forms.CharField(label='Institución', required=False)

# 🔸 Búsqueda: Student
class StudentSearchForm(forms.Form):
    name = forms.CharField(label='Nombre', required=False)
    last_name = forms.CharField(label='Apellido', required=False)
    career = forms.CharField(label='Carrera', required=False)
    college = forms.CharField(label='Institución', required=False)

