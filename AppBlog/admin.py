from django.contrib import admin
from .models import Student, Teacher, Article, Paper

# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Article)
admin.site.register(Paper)