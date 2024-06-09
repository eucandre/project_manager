from django.shortcuts import render
from .models import Project
from .forms import ProjetoForms
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
import mimetypes
# import os module
import os
# Import HttpResponse module
from django.http.response import HttpResponse
from app_tarefas.models import Task

@login_required
def index_to_equipe(request):
    projects = Project.objects.all()
    paginator = Paginator(projects, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        contacts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'app_projects/index.html', {'projects': contacts})


@login_required
def cria_projeto(request):
    if request.method == 'POST':
        form = ProjetoForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/projects/index_projects')
    else:
        form = ProjetoForms()
    return render(request, 'app_projects/new.html', {'form': form})


@login_required
def edit_project(request, nr_item):
    item = Project.objects.get(pk=nr_item)
    if request.method == 'POST':
        form = ProjetoForms(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/projects/index_projects')
    else:
        form = ProjetoForms(instance=item)
    return render(request, 'app_projects/new.html', {'form': form})


@login_required
def view_project(request, nr_item):
    item = Project.objects.get(pk=nr_item)
    tasks = Task.objects.filter(id_project = nr_item)
    return render(request, 'app_projects/show.html', {'item': item, 'tasks':tasks})
