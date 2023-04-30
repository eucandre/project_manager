from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import index,  view, new, edit


app_name = 'app_orgaos'

urlpatterns = [
    path('index_organs', index, name='index_organs'),
    path('organ/<int:id>/', view, name='organ'),
    path('new_organ/', new, name='new_organ'),
    path('edit_organ/<int:id>/', edit, name='edit_organ'),
]
