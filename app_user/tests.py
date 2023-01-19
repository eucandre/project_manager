from django.test import TestCase
from django.test.client import Client
from .models import User


class UserTeste(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        User.objects.create(email='teste@teste.com',
                            name='TESTE UNITARIO PM', password='testelabuild23')
        return super().setUpTestData()

    def teste_labels(self):
        user_teste = User.objects.get(id=1)
        email_field_label = user_teste._meta.get_field('email').verbose_name
        name_field_label = user_teste._meta.get_field('name').verbose_name
        self.assertEquals(email_field_label, 'email')
        self.assertEquals(name_field_label, 'name')

    def teste_descricao_max_length(self):
        user_teste = User.objects.get(id=1)
        max_length = user_teste._meta.get_field('name').max_length
        self.assertEquals(max_length, 254)

    def teste_have_email(self):
        user_teste = User.objects.get(id=1)
        email_user = True if user_teste.email != None else False
        self.assertEquals(email_user, True)

    def teste_is_active(self):
        user_teste = User.objects.get(id=1)
        email_user = True if user_teste.is_active == True else False
        self.assertEquals(email_user, True)

    def teste_is_superuser(self):
        user_teste = User.objects.get(id=1)
        email_user = True if user_teste.is_superuser == False else False
        self.assertEquals(email_user, True)

    def teste_get_client_response(self):
        client = Client()
        log_in = client.post(
            '/accounts/login/', {'username': 'eucandre@gmail.com', 'password': 'testelabuild23'})
        self.assertEquals(log_in.status_code, 200)
