from django.shortcuts import render, redirect, get_object_or_404
from .forms import FormTask, Task, FormChangeStatus
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from app_project.models import Project


def index(request):
    items = Task.objects.all()
    paginator = Paginator(items, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        contacts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'app_tarefas/index.html',{'items':contacts})

def index_by_cli(request):
    items = Task.objects.filter(responsable=request.user)
    paginator = Paginator(items, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        contacts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'app_tarefas/index.html',{'items':contacts})



def new(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = FormTask(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.id_project = project
            item.save()
            return redirect('task_index')
    else:
        form = FormTask()
    return render(request, 'app_tarefas/new.html',{'form':form})


def show(request, id):
    item = Task.objects.get(pk=id)
    return render(request, 'app_tarefas/show.html', {'item': item})

def change_status(request, id):
    item = Task.objects.get(pk = id)
    if request.method == 'POST':
        form = FormChangeStatus(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('task_show',id)
    else:
        form = FormChangeStatus(instance=item)
    return render(request, 'app_tarefas/new.html',{'form':form})


def delete(id):
    item = Task.objects.get(pk = id)
    item.delete()
    return redirect('task_index')
