from django.shortcuts import render
from app_orgaos.forms import Orgaoform
from .models import Organ
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage


@login_required
def index(request):
    items = Organ.objects.filter(active=True).order_by('-id')
    paginator = Paginator(items, 2)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    
    try:
        contacts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'app_orgao/index.html', {'organs': contacts})


@login_required
def view(request, id):
    item = Organ.objects.get(id=id)
    return render(request, 'app_orgao/view.html', {'item': item})


@login_required
def edit(request, id):
    item = Organ.objects.get(id=id)
    return render(request, 'app_orgao/edit.html', {'item': item})


@login_required
def new(request):
    if request.method == 'POST':
        form = Orgaoform(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    else:
        form = Orgaoform()
    return render(request, 'app_orgao/new.html', {'form': form})
