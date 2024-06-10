from django.test import TestCase
from ..forms import Orgaoform

class OrgaoformTestCase(TestCase):
    def test_formorgan_valid(self):
        form_data = {'name': 'TESTE'}
        form = Orgaoform(data=form_data)
        self.assertTrue(form.is_valid())

    def test_formorgan_invalid(self):
        form_data = {'description': ''}
        form = Orgaoform(data=form_data)
        self.assertFalse(form.is_valid())
