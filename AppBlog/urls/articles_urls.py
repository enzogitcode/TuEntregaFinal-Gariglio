from django.urls import path

app_name= 'articles'

from ..views.articles_views import (
     ArticleListView, ArticleCreateView, ArticleUpdateView,
    ArticleDeleteView, ArticleDetailView, ArticleSearchView,
    articles_home,  
)

urlpatterns = [
    path('home/', articles_home, name='home'),
    path('search/', ArticleSearchView.as_view(), name='search'),
    path('', ArticleListView.as_view(), name='list'),
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ArticleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='delete'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='detail'),
]
