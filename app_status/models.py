from django.db import models


class Status(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = 'Status para definir a situação de cada um dos componentes do sistema'
