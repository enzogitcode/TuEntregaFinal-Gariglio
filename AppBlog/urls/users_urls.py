from django.urls import path

app_name= 'users'

from ..models import CustomUser, Teacher, Student

from ..views.user_views import (
    UserRegisterView, 
    LoginView, LogoutView,
    register_choose_your_role,
    AvatarUpdateView,
    user_dashboard,
    CustomLoginView,
    profile,
    users_list,
    ProfileEditView,
    delete_user,
    BasicUserDetailView,
    GenericUserDeleteView
    )
urlpatterns = [
    path('home/', user_dashboard, name='user_home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', profile, name='profile'),
    path('profile_edit/', ProfileEditView.as_view(), name='profile_edit'),
    path('profile/update_avatar/', AvatarUpdateView.as_view(), name='update_avatar'),
    path('register/choose_your_role', register_choose_your_role,  name= 'register_choose_your_role'),
    path('register/user/', UserRegisterView.as_view(), name='register_user'),
    path('login/', LoginView.as_view(template_name='AppBlog/user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('users_list/', users_list, name='list'),
    path('delete/<int:user_id>/', delete_user, name='delete_user'),
    path('basic/<int:pk>/', BasicUserDetailView.as_view(), name='basic_user_detail'),

path('delete/basic_user/<int:pk>/', GenericUserDeleteView.as_view(model=CustomUser), name='delete_basic_user'),
path('delete/student/<int:pk>/', GenericUserDeleteView.as_view(model=Student), name='delete_student'),
path('delete/teacher/<int:pk>/', GenericUserDeleteView.as_view(model=Teacher), name='delete_teacher'),

]