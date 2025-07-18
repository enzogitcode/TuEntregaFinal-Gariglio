from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from ..models import CustomUser
from .TeachersForms import TeacherSelfEditForm
from .StudentsForms import StudentSelfEditForm


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

# 🔹 Edición de datos personales
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

# 🔹 Edición de avatar
class AvatarUploadForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['avatar']
