from django.test import TestCase
from .models import Status


class StatusTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        Status.objects.create(descricao='TESTE UNITARIO')
        return super().setUpTestData()

    def test_descricao_label(self):
        status_teste = Status.objects.get(id=1)
        field_label = status_teste._meta.get_field(
            'descricao').verbose_name
        self.assertEquals(field_label, 'descricao')

    def teste_descricao_max_length(self):
        status_teste = Status.objects.get(id=1)
        max_length = status_teste._meta.get_field('descricao').max_length
        self.assertEquals(max_length, 255)
