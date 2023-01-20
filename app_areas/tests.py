from django.test import TestCase
from .models import Area
from faker import Faker

f = Faker()


class AreaTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        Area.objects.create(descricao=f.name())
        return super().setUpTestData()

    def teste_descricao_label(self):
        area_teste = Area.objects.get(id=1)
        field_label = area_teste._meta.get_field('descricao').verbose_name
        self.assertEquals(field_label, 'descricao')

    def teste_descricao_max_length(self):
        area_teste = Area.objects.get(id=1)
        max_length = area_teste._meta.get_field('descricao').max_length
        self.assertEquals(max_length, 255)

    # def teste_insert_area(self):
