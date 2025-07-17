from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import render
from AppBlog.models import Paper, Profile

def papers_home(request):
    return render(request, 'AppBlog/papers/papers_home.html')

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
    template_name = 'AppBlog/papers/papers_list.html'
    context_object_name= 'papers'
    ordering = ['-date_of_publication']

class PaperDetailView(DetailView):
    model = Paper
    template_name = 'AppBlog/papers/paper_detail.html'
    context_object_name = 'paper'

class PaperCreateView(LoginRequiredMixin, CreateView):
    model = Paper
    fields = ['subject', 'title', 'abstract', 'text_paper']
    template_name = 'AppBlog/paper_create.html'
    success_url = reverse_lazy('home_private')

    def dispatch(self, request, *args, **kwargs):
        # Solo teachers y students pueden crear papers
        try:
            profile = Profile.objects.get(user=request.user)
            if profile.role not in ['teacher', 'student']:
                return render(request, 'AppBlog/forbidden.html')  # Crea este template para mostrar mensaje de acceso denegado
        except Profile.DoesNotExist:
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
    context_object_name = 'papers'

    def test_func(self):
        paper = self.get_object()
        # Solo el autor (teacher/student) o superusuario puede editar
        return self.request.user == paper.author or self.request.user.is_superuser

class PaperDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Paper
    template_name = 'AppBlog/papers/papers_delete_form.html'
    success_url = reverse_lazy('papers_list')
    context_object_name = 'papers'

    def test_func(self):
        paper = self.get_object()
        # Solo el autor (teacher/student) o superusuario puede eliminar
        return self.request.user == paper.author or self.request.user.is_superuser