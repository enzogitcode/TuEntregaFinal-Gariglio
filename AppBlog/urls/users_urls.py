from django.urls import path

app_name= 'users'

from ..views.user_views import (
    UserRegisterView, 
    LoginView, LogoutView,
    home_user,
    register_choose_your_role,
    AvatarUpdateView,
    profile,
    ProfileEditView
    )
urlpatterns = [
    path('profile/avatar/', AvatarUpdateView.as_view(), name='avatar_edit'),
    path('register/choose_your_role', register_choose_your_role,  name= 'register_choose_your_role'),
    path('register/user/', UserRegisterView.as_view(), name='register_user'),
    path('login/', LoginView.as_view(template_name='AppBlog/user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]