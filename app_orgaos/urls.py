from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import index,  view, new, edit


app_name = 'app_orgaos'

urlpatterns = [
    path('index', index, name='index_organs'),
    path('organ/<int:id>/', view, name='organ'),
    path('new/', new, name='new_organ'),
    path('edit/<int:id>/', edit, name='edit_organ'),
]
