from django.urls import path

app_name= 'teachers'

from ..views.teachers_views import (
    TeacherListView, TeacherDeleteView, TeacherDetailView,
TeacherSelfUpdateView, TeacherRegisterView,
TeacherSearchView,
    teachers_home
)

urlpatterns = [
path('home/', teachers_home, name='home'),
    path('teacher/', TeacherRegisterView.as_view(), name='register'),
    path('update/<int:pk>/', TeacherSelfUpdateView.as_view(), name='update'),
    path('', TeacherListView.as_view(), name='list'),
    path('<int:pk>/', TeacherDetailView.as_view(), name='detail'),
    path('search/', TeacherSearchView.as_view(), name='search'),
    path('delete/<int:pk>/', TeacherDeleteView.as_view(), name='delete'),
]