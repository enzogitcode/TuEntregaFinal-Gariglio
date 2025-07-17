from django.urls import path
from .views import views

from .views.articles_views import (
     ArticleListView, ArticleCreateView, ArticleUpdateView,
    ArticleDeleteView, ArticleDetailView, ArticleSearchView,
    articles_home,  
)
from .views.papers_views import (
    PaperListView, PaperCreateView, PaperUpdateView, PaperDeleteView, PaperDetailView,
    PaperSearchView,
    papers_home, 
)
from .views.students_views import (
    StudentListView, StudentDeleteView, StudentDetailView, StudentRegisterView,
    StudentRegisterView, StudentSelfUpdateView, StudentListView,
    StudentDetailView, StudentDeleteView, StudentSearchView,
    students_home
)
from .views.teachers_views import (
    TeacherListView, TeacherDeleteView, TeacherDetailView,
TeacherSelfUpdateView, TeacherRegisterView,
TeacherSearchView,
    teachers_home
)

from .views.user_views import (
    UserRegisterView, 
    LoginView, LogoutView,
    home_user,
    register_choose_your_role,
    AvatarUpdateView
    )

urlpatterns = [
    
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('home_user', home_user, name='home_user'),
    
    # User
        path('profile/avatar/', AvatarUpdateView.as_view(), name='avatar_edit'),
    path('register/choose_your_role', register_choose_your_role,  name= 'register_choose_your_role'),
    path('register/user/', UserRegisterView.as_view(), name='register_user'),
    path('login/', LoginView.as_view(template_name='AppBlog/user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    
    # Students
path('students_home/', students_home, name='students_home'),
    path('register/student/', StudentRegisterView.as_view(), name='register_student'),
    path('students/update/<int:pk>/', StudentSelfUpdateView.as_view(), name='student_self_edit'),
    path('students/', StudentListView.as_view(), name='students_list'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('students/delete/<int:pk>/', StudentDeleteView.as_view(), name='student_delete'),
    path('students_search/', StudentSearchView.as_view(), name='students_search'),

    # Teachers
    path('teachers_home/', teachers_home, name='teachers_home'),
    path('register/teacher/', TeacherRegisterView.as_view(), name='register_teacher'),
    path('teachers/update/<int:pk>/', TeacherSelfUpdateView.as_view(), name='teacher_update_form'),
    path('teachers/', TeacherListView.as_view(), name='teachers_list'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail'),
    path('teachers_search/', TeacherSearchView.as_view(), name='teachers_search'),
    path('teachers/delete/<int:pk>/', TeacherDeleteView.as_view(), name='teacher_delete_form'),

    # Articles
    path('articles_home/', articles_home, name='articles_home'),
    path('articles_search/', ArticleSearchView.as_view() , name='articles_search'),
    path('articles_list/', ArticleListView.as_view(), name='articles_list'),
    path('articles/create/', ArticleCreateView.as_view(), name='create_article_form'),
    path('articles/update/<int:pk>/', ArticleUpdateView.as_view(), name='article_update_form'),
    path('articles/delete/<int:pk>/', ArticleDeleteView.as_view(), name='article_delete_form'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),

    # Papers
    path('papers_home/', papers_home, name='papers_home'),
    path('papers_search/', PaperSearchView.as_view(), name='papers_search'),
    path('papers_list/', PaperListView.as_view(), name='papers_list'),
    path('papers/create/', PaperCreateView.as_view(), name='create_paper_form'),
    path('papers/update/<int:pk>/', PaperUpdateView.as_view(), name='paper_update_form'),
    path('papers/delete/<int:pk>/', PaperDeleteView.as_view(), name='paper_delete_form'),
    path('papers/<int:pk>/', PaperDetailView.as_view(), name='paper_detail'),
]
