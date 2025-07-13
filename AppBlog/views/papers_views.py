from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from ..models import Paper
from django.urls import reverse_lazy
from django.shortcuts import render

def PapersHome(request):
    return render(request, 'AppBlog/papers/papers_home.html')

def papers_search(request):
    return render(request, 'AppBlog/papers/papers_search.html')

def papers_results(request):
    keyword = request.GET.get('keyword', '').strip()
    filtro = request.GET.get('filtro', '')

    if keyword and filtro in ['author_name', 'author_last_name', 'title', 'subject', 'abstract']:
        filtro_kwargs = {f"{filtro}__icontains": keyword}
        papers = Paper.objects.filter(**filtro_kwargs)
    else:
        papers = Paper.objects.none()

    return render(request, 'AppBlog/papers/papers_results.html', {
        'papers': papers,
        'keyword': keyword,
        'filtro': filtro
    })

class PaperListView(ListView):
    model = Paper
    template_name = 'AppBlog/papers/papers_list.html'
    context_object_name= 'papers'

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
    context_object_name= 'papers'

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
    labels= {
        'author_name': 'nombre del autor',
        'author_last_name': 'apellido del autor',
        'author_email': 'email',
        'subject': 'materia',
        'title': 'título',
        'abstract': 'abstract',
        'text_paper': 'texto completo'}
    template_name = 'AppBlog/papers/paper_update_form.html'
    success_url = reverse_lazy('papers_list')
    context_object_name= 'papers'
    

class PaperDeleteView(DeleteView):
    model = Paper
    template_name = 'AppBlog/papers/papers_delete_form.html'
    success_url = reverse_lazy('papers_list')
    context_object_name='papers'
