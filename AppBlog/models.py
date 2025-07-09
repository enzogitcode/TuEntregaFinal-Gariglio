from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    college = models.CharField(max_length=100)
    career= models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"Se creó el estudiante {self.name} {self.last_name} con el correo {self.email}"

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    course = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return f"Se creó el profesor {self.name} {self.last_name} con el correo {self.email}"
    
class Article(models.Model):
    author_name = models.CharField(max_length=100)
    author_last_name = models.CharField(max_length=100)
    author_email = models.EmailField()
    subject = models.CharField(default=list, blank=True)
    date_of_publication = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=200)
    resume = models.CharField(max_length=500)
    text_article = models.TextField()
    def __str__(self):
        return f"Se creó el artículo {self.title} con el autor {self.author_name} y el correo {self.author_email}"
class Paper(models.Model):
    author_name = models.CharField(max_length=100)
    author_last_name = models.CharField(max_length=100)
    author_email = models.EmailField()
    subject = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    abstract = models.CharField(max_length=500)
    text_paper = models.TextField()
    date_of_publication = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"Se creó el artículo {self.title} con el autor {self.autor_name} y el correo {self.autor_email}"
    
    