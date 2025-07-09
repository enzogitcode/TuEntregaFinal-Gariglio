from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from ..models import Paper
from django.urls import reverse_lazy

class PaperListView(ListView):
    model = Paper
    template_name = 'AppBlog/papers/papers_list.html'

class PaperDetailView(DetailView):
    model = Paper
    template_name = 'AppBlog/papers/paper_detail.html'

class PaperCreateView(CreateView):
    model = Paper
    fields = [
        'author_name',
        'author_last_name',
        'author_email',
        'subject',
        'title',
        'abstract',
        'text_paper'
    ]
    template_name = 'AppBlog/papers/create_paper_form.html'
    success_url = reverse_lazy('papers_list')

class PaperUpdateView(UpdateView):
    model = Paper
    fields = [
        'author_name',
        'author_last_name',
        'author_email',
        'subject',
        'title',
        'abstract',
        'text_paper'
    ]
    template_name = 'AppBlog/papers/papers_update_form.html'
    success_url = reverse_lazy('paper_detail')

class PaperDeleteView(DeleteView):
    model = Paper
    template_name = 'AppBlog/papers/papers_delete_form.html'
    success_url = reverse_lazy('app_home')
