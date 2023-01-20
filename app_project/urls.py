from django.urls import path, include
from django.contrib.auth.decorators import login_required

from .views import index_to_equipe, cria_projeto, edit_project, view_project

app_name = 'app_project'

urlpatterns = [
    path('index_projects', index_to_equipe, name='index_projects'),
    path('new_project', cria_projeto, name='new_project'),
    path('edit_project/<nr_item>', edit_project, name='edit_project'),
    path('show_project/<nr_item>', view_project, name='view_project'),
]
