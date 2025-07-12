from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nombre')
    last_name = forms.CharField(max_length=100, label='Apellido')
    age = forms.IntegerField(label='Edad', min_value=0, max_value=120)
    college = forms.CharField(max_length=100, label='Colegio')
    career= forms.CharField(max_length=100, label='Carrera')
    email = forms.EmailField(label='Correo Electrónico')

class TeacherForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nombre')
    last_name = forms.CharField(max_length=100, label='Apellido')
    age = forms.IntegerField(label='Edad', min_value=0, max_value=120)
    course = forms.CharField(max_length=100, label='Curso')
    college = forms.CharField(max_length=100, label='Institución')
    email = forms.EmailField(label='Correo Electrónico')
    
class ArticleForm(forms.Form):
    author_name = forms.CharField(max_length=100, label='Nombre del Autor')
    author_last_name = forms.CharField(max_length=100, label='Apellido del Autor')
    author_email = forms.EmailField(label='Correo Electrónico del Autor')
    subject = forms.CharField(max_length=500, label='Categoría')
    title = forms.CharField(max_length=200, label='Título')
    resume = forms.CharField(widget=forms.Textarea, max_length=500, label='Resumen')
    text_article = forms.CharField(widget=forms.Textarea, label='Texto del Artículo')

class PaperForm(forms.Form):
    author_name = forms.CharField(max_length=100, label='Nombre del Autor')
    author_last_name = forms.CharField(max_length=100, label='Apellido del Autor')
    author_email = forms.EmailField(label='Correo Electrónico del Autor')
    title = forms.CharField(max_length=200, label='Título')
    subject = forms.CharField(max_length=500, label='Categoría')
    abstract = forms.CharField(widget=forms.Textarea, max_length=500, label='Resumen')
    text_paper = forms.CharField(widget=forms.Textarea, label='Texto del Artículo')
