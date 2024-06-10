from django.shortcuts import render, redirect
from .forms import Function, FormFuncion
from django.core.paginator import Paginator, InvalidPage, EmptyPage


def index(request):
    items = Function.objects.all()
    paginator = Paginator(items, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        contacts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'app_function/index.html',{'items':contacts})


def new(request):
    if request.method == 'POST':
        form = FormFuncion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('function_index')
    else:
        form = FormFuncion()
    return render(request, 'app_function/new.html',{'form':form})

def delete(id):
    item = Function.objects.get(pk = id)
    item.delete()
    return redirect('function_index')

