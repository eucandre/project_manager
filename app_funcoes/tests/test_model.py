from django.test import TestCase
from ..models import Function

class FieldTestCase(TestCase):
    def test_field_method(self):
        obj = Function.objects.create(description='Backend')
        self.assertEqual(obj.description, 'Backend')
