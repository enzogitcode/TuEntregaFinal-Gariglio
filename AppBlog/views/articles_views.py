from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from ..models import Article
from django.urls import reverse_lazy

class ArticleListView(ListView):
    model = Article
    template_name = 'AppBlog/articles/articles_list.html'

class ArticleCreateView(CreateView):
    model = Article
    fields = [
        'author_name',
        'author_last_name',
        'author_email',
        'subject',
        'title',
        'resume',
        'text_article'
    ]
    template_name = 'AppBlog/articles/create_article_form.html'
    success_url = reverse_lazy('articles_list')

class ArticleUpdateView(UpdateView):
    model = Article
    fields = [
        'author_name',
        'author_last_name',
        'author_email',
        'subject',
        'title',
        'resume',
        'text_article'
    ]
    template_name = 'AppBlog/articles/articles_update_form.html'
    success_url = reverse_lazy('article_detail')

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'AppBlog/articles/articles_delete_form.html'
    success_url = reverse_lazy('app_home')
