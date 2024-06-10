from django.test import TestCase
from ..models import Organ

class OrganTestCase(TestCase):
    def test_ogan_method(self):
        obj = Organ.objects.create(name='TESTE')
        self.assertEqual(obj.name, 'TESTE')
