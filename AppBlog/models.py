from django.db import models
from django.contrib.auth.models import AbstractUser

# Usuario base personalizado
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    ROLE_CHOICES = [
        ('user', 'User'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    def __str__(self):
        return f"{self.username} ({self.role})"


# Teacher con campos extra
class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"Teacher: {self.user.username}"


# Student con campos extra
class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    career = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"Student: {self.user.username}"


# Artículos
class Article(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    date_of_publication = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=200)
    resume = models.CharField(max_length=500)
    text_article = models.TextField()

    def __str__(self):
        return f"Artículo '{self.title}' por {self.author.get_full_name()} ({self.author.email})"


# Papers
class Paper(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    abstract = models.CharField(max_length=500)
    text_paper = models.TextField()
    date_of_publication = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Paper '{self.title}' por {self.author.get_full_name()} ({self.author.email})"
# Modelo para avatar de usuario
class Avatar(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='avatar_imagenes')
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"