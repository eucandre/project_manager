from django.db import models
import pytest



class Field(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name_plural = 'Áreas de classificação de cada projeto'
    
@pytest.mark.django_db
def test_seu_modelo_creation():
    instance = Field.objects.create(description='Construção')
    assert instance.pk is not None
