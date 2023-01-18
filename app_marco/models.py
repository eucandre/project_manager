from django.db import models
from app_user.models import User


class Marco(models.Model):
    titulo = models.CharField(max_length=255)
    inicio = models.DateField()
    fim = models.DateField()
    objetivo = models.TextField()
    integrantes = models.ManyToManyField(
        User)
    responsavel = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='names')
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = 'Marco de tarefas realizadas'
