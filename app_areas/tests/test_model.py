from django.test import TestCase
from ..models import Field

class FieldTestCase(TestCase):
    def test_field_method(self):
        obj = Field.objects.create(description='desenvolvimento')
        self.assertEqual(obj.description, 'desenvolvimento')
