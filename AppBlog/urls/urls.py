from django.urls import path, include

urlpatterns = [
    path('papers/', include('AppBlog.urls.papers_urls')),
    path('articles/', include('AppBlog.urls.articles_urls')),
    path('students/', include('AppBlog.urls.students_urls')),
    path('teachers/', include('AppBlog.urls.articles_urls')),
]
