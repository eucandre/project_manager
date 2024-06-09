from django.db import models


class Function(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = 'Função de cada um dos contribuintes do projeto'
