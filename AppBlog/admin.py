from django.contrib import admin
from .models import Student, Teacher, Article, Paper, Avatar, CustomUser


# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Article)
admin.site.register(Paper)
admin.site.register(Avatar)
admin.site.register(CustomUser)
