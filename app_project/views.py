from django.shortcuts import render
from .models import Projeto
from .forms import ProjetoForms
from django.core.paginator import Paginator, InvalidPage, EmptyPage


def index_to_equipe(request):
    projects = Projeto.objects.all()  # get(responsavel=request.user.id)
    paginator = Paginator(projects, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # Se o page request (9999) está fora da lista, mostre a última página.
    try:
        contacts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'app_projects/index.html', {'projects': contacts})


def cria_projeto(request):
    if request.method == 'POST':
        form = ProjetoForms(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProjetoForms()
    return render(request, 'app_projects/new.html', {'form': form})
