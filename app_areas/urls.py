from django.urls import path
from .views import index, new, delete, upload


urlpatterns = [
    path('index/', index, name='area_index'),
    path('new/', new),
    path('delete/<int:id>', delete),
    path('upload/', upload, name='upload_area'),
]