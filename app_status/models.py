from django.db import models


class Status(models.Model):
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = 'Status para definir a situação de cada um dos componentes do sistema'
