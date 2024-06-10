from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import index

class IndexUrlestCase(SimpleTestCase):
    def test_index_url_resolves(self):
        url = reverse('area_index')
        self.assertEqual(resolve(url).func, index)
