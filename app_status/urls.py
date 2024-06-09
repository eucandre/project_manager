from django.urls import path
from .views import index, new, delete


urlpatterns = [
    path('index/', index, name='status_index'),
    path('new/', new),
    path('delete/<int:id>', delete),
]