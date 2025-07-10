from django.urls import path
from .views import views


from .views.articles_views import (
    ArticleListView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView, ArticleDetailView,
    ArticlesHome
)
from .views.papers_views import (
    PaperListView, PaperCreateView, PaperUpdateView, PaperDeleteView, PaperDetailView,
    PapersHome
)
from .views.students_views import (
    StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView, StudentDetailView,
    StudentsHome
)
from .views.teachers_views import (
    TeacherListView, TeacherCreateView, TeacherUpdateView, TeacherDeleteView, TeacherDetailView,
    TeachersHome
)



urlpatterns = [
    path('', views.home, name='home'),

    # Students
path('students_home/', StudentsHome, name='students_home'),
    path('students_list/', StudentListView.as_view(), name='students_list'),
    path('students/create/', StudentCreateView.as_view(), name='student_create'),
    path('students/update/<int:pk>/', StudentUpdateView.as_view(), name='student_update'),
    path('students/delete/<int:pk>/', StudentDeleteView.as_view(), name='student_delete'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),

    # Teachers
    path('teachers_home/', TeachersHome, name='teachers_home'),
    path('teachers/', TeacherListView.as_view(), name='teachers_list'),
    path('teachers/create/', TeacherCreateView.as_view(), name='teacher_create'),
    path('teachers/update/<int:pk>/', TeacherUpdateView.as_view(), name='teacher_update'),
    path('teachers/delete/<int:pk>/', TeacherDeleteView.as_view(), name='teacher_delete'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail'),

    # Articles
    path('articles_home/', ArticlesHome, name='articles_home'),
    path('articles_list/', ArticleListView.as_view(), name='articles_list'),
    path('articles/create/', ArticleCreateView.as_view(), name='article_create'),
    path('articles/update/<int:pk>/', ArticleUpdateView.as_view(), name='article_update'),
    path('articles/delete/<int:pk>/', ArticleDeleteView.as_view(), name='article_delete'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),

    # Papers
    path('papers_home/', PapersHome, name='papers_home'),
    path('papers_list/', PaperListView.as_view(), name='papers_list'),
    path('papers/create/', PaperCreateView.as_view(), name='paper_create'),
    path('papers/update/<int:pk>/', PaperUpdateView.as_view(), name='paper_update'),
    path('papers/delete/<int:pk>/', PaperDeleteView.as_view(), name='paper_delete'),
    path('papers/<int:pk>/', PaperDetailView.as_view(), name='paper_detail'),
]


