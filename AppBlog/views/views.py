from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import Article, Paper
from django.http import HttpResponseNotFound

def home(request):
    return render(request, 'AppBlog/home.html')

def about(request):
    return render(request, 'AppBlog/about.html')

def shared_home(request, section):
    sections = {
        'articles': {
            'title': 'Artículos informativos',
            'list_url': 'articles:list',
            'search_url': 'articles:search',
            'create_url': 'articles:create',
            'detail_url': 'articles:detail',
            'allow_create': True
        },
        'papers': {
            'title': 'Papers académicos',
            'list_url': 'papers:list',
            'search_url': 'papers:search',
            'create_url': 'papers:create',
            'detail_url': 'papers:detail',
            'allow_create': True
        },
        'teachers': {
            'title': 'Panel de Docentes',
            'list_url': 'teachers:list',
            'search_url': 'teachers:search',
            'create_url': None,
            'detail_url': 'teachers:detail',
            'allow_create': False
        },
        'students': {
            'title': 'Panel de Estudiantes',
            'list_url': 'students:list',
            'search_url': 'students:search',
            'create_url': None,
            'detail_url': 'students:detail',
            'allow_create': False
        }
    }

    config = sections.get(section)
    if not config:
        return HttpResponseNotFound("Sección no válida")

    can_create = (
        config['allow_create'] and
        request.user.is_authenticated and
        (request.user.role in ['teacher', 'student'] or request.user.is_superuser)
    )

    content_list = []  # podés reemplazar esto por una consulta real si querés mostrar contenido

    return render(request, 'AppBlog/shared/shared_home.html', {
        'title': config['title'],
        'list_url': config['list_url'],
        'search_url': config['search_url'],
        'create_url': config['create_url'],
        'detail_url': config['detail_url'],
        'can_create': can_create,
        'section': section,
        'user': request.user,
        'content_list': content_list
    })
