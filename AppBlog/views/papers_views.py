from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import render
from AppBlog.models import Paper


# def papers_home(request):
#     context ={}
#     context["user_create"] = request.user.is_authenticated and (request.user.role in ["teacher", "student"] or request.user.is_superuser)
#     return render(request, 'AppBlog/papers/papers_home.html', context)

class PaperSearchView(ListView):
    model = Paper
    template_name = 'AppBlog/shared/search.html'
    context_object_name = 'papers'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Paper.objects.filter(
                Q(title__icontains=query) |
                Q(abstract__icontains=query) |
                Q(subject__icontains=query) |
                Q(author__first_name__icontains=query) |
                Q(author__last_name__icontains=query) |
                Q(author__email__icontains=query) |
                Q(date_of_publication__icontains=query)
            ).distinct()
        return Paper.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        context['tipo'] = 'Artículo'
        context['detail_url'] = 'articles:detail'
        return context

class PaperListView(ListView):
    model = Paper
    template_name = 'AppBlog/shared/list_publications.html'
    context_object_name = 'items'
    extra_context = {
        'tipo': 'Papers',
        'detail_url': 'papers:detail',
        'create_url': 'papers:create',
        'show_create_button': True
    }

class PaperDetailView(DetailView):
    model = Paper
    template_name = 'AppBlog/shared/detail.html'
    context_object_name = 'obj'
    extra_context = {
        'tipo': 'Paper'
    }

class PaperCreateView(LoginRequiredMixin, CreateView):
    model = Paper
    fields = ['subject', 'title', 'abstract', 'text_paper']
    template_name = 'AppBlog/shared/create.html'
    success_url = reverse_lazy('papers:list')
    extra_context = { 'tipo': 'Paper' }

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.role not in ['teacher', 'student']:
            return render(request, 'AppBlog/forbidden.html')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PaperUpdateView(UpdateView):
    model = Paper
    fields = ['title', 'subject', 'abstract', 'text_paper']
    template_name = 'AppBlog/shared/update.html'
    context_object_name = 'obj'
    success_url= reverse_lazy('papers:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipo'] = 'Paper'
        return context

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != request.user or request.user.role not in ['teacher', 'student']:
            return HttpResponseForbidden("No tenés permiso para editar este paper.")
        return super().dispatch(request, *args, **kwargs)


    def test_func(self):
        paper = self.get_object()
        return self.request.user == paper.author or self.request.user.is_superuser

class PaperDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Paper
    template_name = 'AppBlog/papers/papers_delete_form.html'
    success_url = reverse_lazy('papers_list')
    context_object_name = 'paper'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipo'] = 'Paper'  
        context['cancel_url'] = reverse_lazy('papers:list')  
        return context

    def test_func(self):
        paper = self.get_object()
        return self.request.user == paper.author or self.request.user.is_superuser
