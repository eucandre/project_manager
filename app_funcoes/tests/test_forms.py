from django.test import TestCase
from ..forms import FormFuncion

class FormFuncionTestCase(TestCase):
    def test_formfield_valid(self):
        form_data = {'description': 'Backend'}
        form = FormFuncion(data=form_data)
        self.assertTrue(form.is_valid())

    def test_formfield_invalid(self):
        form_data = {'description': ''}
        form = FormFuncion(data=form_data)
        self.assertFalse(form.is_valid())
