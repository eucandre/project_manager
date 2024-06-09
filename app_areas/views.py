from django.shortcuts import render, redirect
from .models import Field
from .forms import FormUpload, FormField
from django.core.files.storage import default_storage
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib.auth.decorators import login_required
import csv

class FilesManager:
    
    ''' Class to maintence upload and read files contents.
        It's very important class to large data volume.
    '''

    def read_csv_file_return_rows(self, file_path, class_operation):
        ppa_actions = []
        with open(file_path, encoding='utf8') as file:
            rows = csv.DictReader(file)
            for row in rows:
              ppa_action = class_operation(name = row['name'])
              ppa_actions.append(ppa_action)  
        class_operation.objects.bulk_create(ppa_actions)

    def delete_old_registers(self, class_name):
        class_name.objects.all().delete()


def get_instance_class(class_name):
    return class_name()

def index(request):
    items = Field.objects.all()
    paginator = Paginator(items, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        contacts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'app_area/index.html',{'items':contacts})

def new(request):
    if request.method == 'POST':
        form = FormField(request.POST)
        if form.is_valid():
            form.save()
            return redirect('area_index')
    else:
        form = FormField()
    return render(request, 'app_area/new.html',{'form':form})

def delete(id):
    item = Field.objects.get(pk = id)
    item.delete()
    return redirect('area_index')

def upload(request):
    object_instance = get_instance_class(FilesManager)
    if request.method == 'POST':
        form = FormUpload(request.POST, request.FILES)
        if form.is_valid():
            file_uploaded = request.FILES.get('file')
            if file_uploaded:
                file_path = default_storage.save(file_uploaded.name, file_uploaded)
                file_path = default_storage.path(file_path)
                object_instance.delete_old_registers(Field)
                object_instance.read_csv_file_return_rows(file_path, Field)
                return redirect('#')
                
    else:
        form = FormUpload()
    return render(request, 'app_area/upload.html', {'form': form})
