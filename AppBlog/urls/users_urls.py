from django.urls import path

app_name= 'users'

from ..views.user_views import (
    UserRegisterView, 
    LoginView, LogoutView,
    register_choose_your_role,
    AvatarUpdateView,
    user_dashboard,
    CustomLoginView,
    profile,
    users_list,
    ProfileEditView
    
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
    path('users_list/', users_list, name='users_list'),
]