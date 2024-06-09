from django.test import TestCase
from .models import Function


class FuncaoTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        Function.objects.create(descricao='TESTE UNITARIO')
        return super().setUpTestData()

    def teste_descricao_label(self):
        funcao_teste = Function.objects.get(id=1)
        field_label = funcao_teste._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'descricao')

    def teste_descricao_max_length(self):
        funcao_teste = Function.objects.get(id=1)
        max_length = funcao_teste._meta.get_field('description').max_length
        self.assertEquals(max_length, 255)
