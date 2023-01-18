from django.db import models


class Funcao(models.Model):
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = 'Função de cada um dos contribuintes do projeto'
