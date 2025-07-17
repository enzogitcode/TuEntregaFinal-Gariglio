from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from AppBlog.models import Article
from django.db.models import Q

def articles_home(request):
    context ={}
    context["user_create"] = request.user.is_authenticated and (request.user.role in ["teacher", "student"] or request.user.is_superuser)
    return render(request, 'AppBlog/articles/articles_home.html', context)

class ArticleListView(ListView):
    model = Article
    template_name = 'AppBlog/articles/articles_list.html'
    context_object_name = 'articles'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'AppBlog/articles/article_detail.html'
    context_object_name = 'article'

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['subject', 'title', 'resume', 'text_article']
    template_name = 'AppBlog/articles/create_article_form.html'
    success_url = reverse_lazy('articles_list')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.role not in ['teacher', 'student']:
            return render(request, 'AppBlog/forbidden.html')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ['subject', 'title', 'resume', 'text_article']
    template_name = 'AppBlog/articles/article_update_form.html'
    success_url = reverse_lazy('articles_list')

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author or self.request.user.is_superuser

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'AppBlog/articles/article_delete_form.html'
    success_url = reverse_lazy('articles_list')

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author or self.request.user.is_superuser

class ArticleSearchView(ListView):
    model = Article
    template_name = 'AppBlog/articles/articles_search.html'
    context_object_name = 'articles'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Article.objects.filter(
                Q(title__icontains=query) |
                Q(resume__icontains=query) |
                Q(subject__icontains=query) |
                Q(author__first_name__icontains=query) |
                Q(author__last_name__icontains=query) |
                Q(author__email__icontains=query) |
                Q(date_of_publication__icontains=query)
            ).distinct()
        return Article.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context
