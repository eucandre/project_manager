from django.db import models
from app_user.models import User
from app_areas.models import Area
from app_status.models import Status


class Projeto(models.Model):
    titulo = models.CharField(max_length=255)
    inicio = models.DateField()
    fim = models.DateField()
    custo = models.FloatField(blank=True, null=True)
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name='state_project')
    objetivo = models.TextField()
    area = models.ManyToManyField(Area, related_name='field')
    integrantes = models.ManyToManyField(
        User)
    responsavel = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='responseble')
    attachment = models.FileField(upload_to='tarefas', blank=True, null=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return "/projects/%i/" % (self.pk)

    class Meta:
        verbose_name_plural = 'Projetos'
