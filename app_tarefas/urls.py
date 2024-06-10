from django.urls import path
from .views import index, new, delete, show, change_status, index_by_cli


urlpatterns = [
    path('index/', index, name='task_index'),
    path('index_by_cli/', index_by_cli, name='task_index_by_cli'),
    path('new/<int:project_id>', new),
    path('show/<int:id>', show, name='task_show'),
    path('changestatus/<int:id>', change_status, name='task_change'),
    path('delete/<int:id>', delete),
]