from django.urls import path
from .views import views

from .views.articles_views import (
    ArticleListView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView, ArticleDetailView,
    ArticlesHome, articles_results, articles_search, 
)
from .views.papers_views import (
    PaperListView, PaperCreateView, PaperUpdateView, PaperDeleteView, PaperDetailView,
    PapersHome, papers_search, papers_results
)
from .views.students_views import (
    StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView, StudentDetailView,
    StudentsHome, students_search, students_results
)
from .views.teachers_views import (
    TeacherListView, TeacherCreateView, TeacherUpdateView, TeacherDeleteView, TeacherDetailView,
    teachers_home, teachers_search, teachers_results
)

from .views.user_views import RegisterView, EditUserView, CustomLoginView, LoginView, LogoutView

urlpatterns = [
    
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    
    # User
    path('register/', RegisterView.as_view(), name='register'),
    path('edit/', EditUserView.as_view(), name='edit_user'),
    path('login/', LoginView.as_view(template_name='AppBlog/user/login.html'), name='login'),
        path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    #path('logout/', LogoutView.as_view(template_name='AppBlog/user/logout.html'), name='logout'),
    
    # Students
path('students_home/', StudentsHome, name='students_home'),
path('students_search/', students_search, name='students_search'),
    path('students_results/', students_results, name='students_results'),
    path('students_list/', StudentListView.as_view(), name='students_list'),
    path('students/create/', StudentCreateView.as_view(), name='create_student_form'),
    path('students/update/<int:pk>/', StudentUpdateView.as_view(), name='student_update_form'),
    path('students/delete/<int:pk>/', StudentDeleteView.as_view(), name='student_delete_form'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),

    # Teachers
    path('teachers_home/', teachers_home, name='teachers_home'),
    path('teachers_search/', teachers_search, name='teachers_search'),
    path('teachers_results/', teachers_results, name='teachers_results'),
    path('teachers/', TeacherListView.as_view(), name='teachers_list'),
    path('teachers/create_teacher_form/', TeacherCreateView.as_view(), name='create_teacher_form'),
    path('teachers/update/<int:pk>/', TeacherUpdateView.as_view(), name='teacher_update_form'),
    path('teachers/delete/<int:pk>/', TeacherDeleteView.as_view(), name='teacher_delete_form'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail'),

    # Articles
    path('articles_home/', ArticlesHome, name='articles_home'),
    path('articles_search/', articles_search, name='articles_search'),
    path('articles_results/', articles_results, name='articles_results'),
    path('articles_list/', ArticleListView.as_view(), name='articles_list'),
    path('articles/create/', ArticleCreateView.as_view(), name='create_article_form'),
    path('articles/update/<int:pk>/', ArticleUpdateView.as_view(), name='article_update_form'),
    path('articles/delete/<int:pk>/', ArticleDeleteView.as_view(), name='article_delete_form'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),

    # Papers
    path('papers_home/', PapersHome, name='papers_home'),
    path('papers_search/', papers_search, name='papers_search'),
    path('papers_results/', papers_results, name='papers_results'),
    path('papers_list/', PaperListView.as_view(), name='papers_list'),
    path('papers/create/', PaperCreateView.as_view(), name='create_paper_form'),
    path('papers/update/<int:pk>/', PaperUpdateView.as_view(), name='paper_update_form'),
    path('papers/delete/<int:pk>/', PaperDeleteView.as_view(), name='paper_delete_form'),
    path('papers/<int:pk>/', PaperDetailView.as_view(), name='paper_detail'),
]


