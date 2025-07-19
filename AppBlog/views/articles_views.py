from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from AppBlog.models import Article
from django.db.models import Q
from django.http import HttpResponseForbidden

# def articles_home(request):
#     context ={}
#     context["user_create"] = request.user.is_authenticated and (request.user.role in ["teacher", "student"] or request.user.is_superuser)
#     return render(request, 'AppBlog/articles/articles_home.html', context)

class ArticleListView(ListView):
    model = Article
    template_name = 'AppBlog/shared/list.html'
    context_object_name = 'items'
    extra_context = {
        'tipo': 'Artículos',
        'detail_url': 'articles:detail',
        'create_url': 'articles:create',
        'show_create_button': True
    }


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'AppBlog/shared/detail.html'
    context_object_name = 'obj'
    extra_context = {
        'tipo': 'Artículo'
    }

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['subject', 'title', 'resume', 'text_article']
    template_name = 'AppBlog/shared/create.html'
    success_url = reverse_lazy('articles:list')
    extra_context = { 'tipo': 'Artículo' }

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.role not in ['teacher', 'student']:
            return render(request, 'AppBlog/forbidden.html')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'subject', 'resume', 'text_article']
    template_name = 'AppBlog/shared/update.html'
    context_object_name = 'obj'
    success_url= reverse_lazy('articles:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipo'] = 'Artículo'
        return context

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != request.user or request.user.role not in ['teacher', 'student']:
            return HttpResponseForbidden("No tenés permiso para editar este artículo.")
        return super().dispatch(request, *args, **kwargs)

    def test_func(self):
        obj = self.get_object()
        return self.request.user.id == obj.author.id


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    context_object_name = 'obj'  
    template_name = 'AppBlog/shared/delete.html'
    success_url = reverse_lazy('articles:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipo'] = 'Artículo'  
        context['cancel_url'] = 'articles:list'  
        return context

    def test_func(self):
        obj = self.get_object()
        return self.request.user.id == obj.author.id or self.request.user.is_superuser


class ArticleSearchView(ListView):
    model = Article
    template_name = 'AppBlog/shared/search.html'
    context_object_name = 'items'

    def get_queryset(self):
        query = self.request.GET.get('q', '').strip()
        if query:
            return Article.objects.filter(
                Q(title__icontains=query) |
                Q(resume__icontains=query) |
                Q(subject__icontains=query) |
                Q(author__first_name__icontains=query) |
                Q(author__last_name__icontains=query) |
                Q(author__email__icontains=query)
            ).distinct()
        return Article.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        context['tipo'] = 'Artículo'
        context['detail_url'] = 'articles:detail'
        return context

