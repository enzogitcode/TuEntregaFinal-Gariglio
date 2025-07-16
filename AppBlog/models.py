from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    age= models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - Docente"

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    career = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - Estudiante"
    
class Article(models.Model):
    author_name = models.CharField(max_length=100)
    author_last_name = models.CharField(max_length=100)
    author_email = models.EmailField()
    subject = models.CharField(max_length=200)
    date_of_publication = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=200)
    resume = models.CharField(max_length=500)
    text_article = models.TextField()
    def __str__(self):
        return f"Se creó el artículo {self.title} con el autor {self.author_name} y el correo {self.author_email}"
    

class Paper(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    abstract = models.CharField(max_length=500)
    text_paper = models.TextField()
    date_of_publication = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Paper '{self.title}' creado por {self.author.get_full_name()} ({self.author.email})"

    
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank =True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"


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
    

