from django.db import models
from django.contrib.auth.models import User

# Perfil extendido para distinguir roles
class Profile(models.Model):
    ROLE_CHOICES = [
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ('user', 'User'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# Modelo Teacher con campos extra
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - Docente"

# Modelo Student con campos extra
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    career = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - Estudiante"

# Modelo para artículos informativos
class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    date_of_publication = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=200)
    resume = models.CharField(max_length=500)
    text_article = models.TextField()

    def __str__(self):
        return f"Artículo '{self.title}' por {self.author.get_full_name()} ({self.author.email})"

# Modelo para papers
class Paper(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    abstract = models.CharField(max_length=500)
    text_paper = models.TextField()
    date_of_publication = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Paper '{self.title}' creado por {self.author.get_full_name()} ({self.author.email})"

# Modelo para avatar de usuario
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"