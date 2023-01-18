from django.db import models
from app_marco.models import Marco
from app_user.models import User
from app_status.models import Status


class Tarefa(models.Model):
    titulo = models.CharField(max_length=255)
    id_marco = models.ForeignKey(
        Marco, on_delete=models.CASCADE, blank=True, null=True)
    objetivo = models.TextField()
    custo = models.FloatField(blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='state_task')
    responsavel = models.ForeignKey(User, on_delete=models.CASCADE)
    dependencias = models.CharField(max_length=255, blank=True, null=True)
    inicio = models.DateField()
    fim = models.DateField()

    def __str__(self):
        return self.titulo
       
    class Meta:
        verbose_name_plural = 'Tarefas a serem realizadas'
    
    