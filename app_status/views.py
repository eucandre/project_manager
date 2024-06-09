from django.shortcuts import render, redirect
from .forms import FormStatus, Status
from django.core.paginator import Paginator, InvalidPage, EmptyPage


def index(request):
    items = Status.objects.all()
    paginator = Paginator(items, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        contacts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'app_status/index.html',{'items':contacts})

def new(request):
    if request.method == 'POST':
        form = FormStatus(request.POST)
        if form.is_valid():
            form.save()
            return redirect("status_index")
    else:
        form = FormStatus()
    return render(request, 'app_status/new.html', {'form':form})

def delete(id):
    item = Status.objects.get(pk = id)
    item.delete()
    return redirect("status_index")

