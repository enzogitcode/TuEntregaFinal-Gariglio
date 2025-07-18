from django.urls import path, include
from ..views.views import home, shared_home, about

urlpatterns = [
    path('', home, name='home'),
    path('about/', home, name='about'),
    path('home/<str:section>/', shared_home, name='shared_home'),
    path('articles/', include('AppBlog.urls.articles_urls')),
    path('papers/', include('AppBlog.urls.papers_urls')),
    path('students/', include('AppBlog.urls.students_urls')),
    path('teachers/', include('AppBlog.urls.teachers_urls')),
    path('users/', include('AppBlog.urls.users_urls')),
]
