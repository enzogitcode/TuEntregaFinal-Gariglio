from django.urls import path
app_name = 'papers'

from ..views.papers_views import (
    PaperListView, PaperCreateView, PaperUpdateView, PaperDeleteView, PaperDetailView,
    PaperSearchView,
    papers_home, 
)

urlpatterns = [
    path('home/', papers_home, name='home'),
    path('search/', PaperSearchView.as_view(), name='search'),
    path('', PaperListView.as_view(), name='list'),
    path('create/', PaperCreateView.as_view(), name='create'),
    path('update/<int:pk>/', PaperUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', PaperDeleteView.as_view(), name='delete'),
    path('<int:pk>/', PaperDetailView.as_view(), name='detail'),
]
