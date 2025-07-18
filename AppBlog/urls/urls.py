from django.urls import path, include
from ..views.views import home

urlpatterns = [
    path('', home, name='home'),
    path('articles/', include('AppBlog.urls.articles_urls')),
    path('papers/', include('AppBlog.urls.papers_urls')),
    path('students/', include('AppBlog.urls.students_urls')),
    path('teachers/', include('AppBlog.urls.teachers_urls')),
    path('users/', include('AppBlog.urls.users_urls')),
]
