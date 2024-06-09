from django.test import TestCase
from .models import Organ
from faker import Faker

f = Faker()


class OrganTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        Organ.objects.create(name=f.name())
        return super().setUpTestData()

    def teste_name_max_length(self):
        funcao_teste = Organ.objects.get(id=1)
        max_length = funcao_teste._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)

    def teste_cep_max_length(self):
        funcao_teste = Organ.objects.get(id=1)
        max_length = funcao_teste._meta.get_field('cep').max_length
        self.assertEquals(max_length, 255)

    def teste_address_max_length(self):
        funcao_teste = Organ.objects.get(id=1)
        max_length = funcao_teste._meta.get_field('address').max_length
        self.assertEquals(max_length, 255)

    def teste_acronym_max_length(self):
        funcao_teste = Organ.objects.get(id=1)
        max_length = funcao_teste._meta.get_field('acronym').max_length
        self.assertEquals(max_length, 255)
