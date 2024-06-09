from django.db import models


class Field(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description
    
    
    class Meta:
        verbose_name_plural = 'Áreas de classificação de cada projeto'
    