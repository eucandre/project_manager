from django.db import models
from app_marco.models import Marco
from app_user.models import User


class Tarefa(models.Model):
    titulo = models.CharField(max_length=255)
    id_marco = models.ForeignKey(
        Marco, on_delete=models.CASCADE, blank=True, null=True)
    objetivo = models.TextField()
    responsavel = models.ForeignKey(User, on_delete=models.CASCADE)
    dependencias = models.CharField(max_length=255, blank=True, null=True)
    inicio = models.DateField()
    fim = models.DateField()

    def __str__(self):
        return self.titulo
       
    class Meta:
        verbose_name_plural = 'Tarefas a serem realizadas'
    
    