from django.db import models


class Area(models.Model):
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao
    
    
    class Meta:
        verbose_name_plural = 'Áreas de classificação de cada projeto'
    