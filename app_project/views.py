from django.shortcuts import render
from .models import Projeto
from .forms import ProjetoForms


def index_to_equipe(request):
    projects = Projeto.objects.all()  # get(responsavel=request.user.id)
    return render(request, 'app_projects/index.html', {'projects': projects})


def cria_projeto(request):
    if request.method == 'POST':
        form = ProjetoForms(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProjetoForms()
    return render(request, 'app_projects/new.html', {'form': form})
