from django.urls import path

app_name= 'students'

from ..views.students_views import (
    students_home, 
    StudentRegisterView,
    StudentListView,
    StudentDetailView,
    StudentSearchView,
    StudentDeleteView,
    StudentSelfUpdateView,
    )


urlpatterns = [
    path('home/', students_home, name='home'),
    path('student/', StudentRegisterView.as_view(), name='register'),
    path('update/<int:pk>/', StudentSelfUpdateView.as_view(), name='update'),
    path('', StudentListView.as_view(), name='list'),
    path('<int:pk>/', StudentDetailView.as_view(), name='detail'),
    path('search/', StudentSearchView.as_view(), name='search'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='delete'),
]
