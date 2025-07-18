from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import render
from AppBlog.models import Paper

def papers_home(request):
    context ={}
    context["user_create"] = request.user.is_authenticated and (request.user.role in ["teacher", "student"] or request.user.is_superuser)
    return render(request, 'AppBlog/papers/papers_home.html', context)

class PaperSearchView(ListView):
    model = Paper
    template_name = 'AppBlog/papers/papers_search.html'
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
        return context

class PaperListView(ListView):
    model = Paper
    template_name = 'AppBlog/shared/list.html'
    context_object_name = 'items'
    ordering = ['-date_of_publication']
    extra_context = {
        'tipo': 'Papers',
        'detail_url': 'papers:detail',
        'create_url': 'papers:create',
        'show_create_button': True
    }

class PaperDetailView(DetailView):
    model = Paper
    template_name = 'AppBlog/papers/paper_detail.html'
    context_object_name = 'paper'

class PaperCreateView(LoginRequiredMixin, CreateView):
    model = Paper
    fields = ['subject', 'title', 'abstract', 'text_paper']
    template_name = 'AppBlog/papers/create_paper_form.html'
    success_url = reverse_lazy('papers:list')
    extra_context = { 'tipo': 'Paper' }

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.role not in ['teacher', 'student']:
            return render(request, 'AppBlog/forbidden.html')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PaperUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Paper
    fields = ['subject', 'title', 'abstract', 'text_paper']
    template_name = 'AppBlog/papers/paper_update_form.html'
    success_url = reverse_lazy('papers_list')
    context_object_name = 'paper'

    def test_func(self):
        paper = self.get_object()
        return self.request.user == paper.author or self.request.user.is_superuser

class PaperDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Paper
    template_name = 'AppBlog/papers/papers_delete_form.html'
    success_url = reverse_lazy('papers_list')
    context_object_name = 'paper'

    def test_func(self):
        paper = self.get_object()
        return self.request.user == paper.author or self.request.user.is_superuser
