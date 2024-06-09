from django.urls import path
from .views import index, new, delete


urlpatterns = [
    path('index/', index, name='task_index'),
    path('new/<int:project_id>', new),
    path('delete/<int:id>', delete),
]