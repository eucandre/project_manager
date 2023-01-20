from django.db import models
from app_marco.models import Marco
from app_project.models import Projeto
from app_user.models import User
from app_status.models import Status
from django.utils import timezone


class Tarefa(models.Model):
    titulo = models.CharField(max_length=255)
    id_project = models.ForeignKey(
        Projeto, on_delete=models.CASCADE, related_name= 'project_of_the_task')
    id_marco = models.ForeignKey(
        Marco, on_delete=models.CASCADE, blank=True, null=True)
    objetivo = models.TextField()
    custo = models.FloatField(blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='state_task')
    responsavel = models.ForeignKey(User, on_delete=models.CASCADE)
    dependencias = models.CharField(max_length=255, blank=True, null=True)
    attachment = models.FileField(upload_to='tarefas',blank=True, null=True)
    inicio = models.DateField()
    fim = models.DateField()
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(default=None)

    def __str__(self):
        return self.titulo
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        self.updated_at = timezone.now()
        return super(User, self).save(*args, **kwargs)
       
    class Meta:
        verbose_name_plural = 'Tarefas a serem realizadas'
    
    