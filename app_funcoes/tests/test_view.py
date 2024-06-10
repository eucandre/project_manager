from django.test import TestCase
from django.urls import reverse

class FieldTestCase(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('function_index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 200)