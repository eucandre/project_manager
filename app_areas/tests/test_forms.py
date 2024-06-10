from django.test import TestCase
from ..forms import FormField

class FormFieldTestCase(TestCase):
    def test_formfield_valid(self):
        form_data = {'description': 'Desenvolvimento'}
        form = FormField(data=form_data)
        self.assertTrue(form.is_valid())

    def test_formfield_invalid(self):
        form_data = {'description': ''}
        form = FormField(data=form_data)
        self.assertFalse(form.is_valid())
