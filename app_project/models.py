from django.db import models
from app_user.models import User
from app_areas.models import Area


class Projeto(models.Model):
    titulo = models.CharField(max_length=255)
    inicio = models.DateField()
    fim = models.DateField()
    custo = models.FloatField(blank=True, null=True)
    objetivo = models.TextField()
    area = models.ForeignKey(
        Area, on_delete=models.CASCADE, related_name='field')
    integrantes = models.ManyToManyField(
        User)
    responsavel = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='responseble')
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = 'Projetos'
