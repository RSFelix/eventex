from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Rogerio Felix', cpf='12345678901',
                    email='rogerio@felix.net', phone='86-99818-1818')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'rogerio@felix.net']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = ['Rogerio Felix',
                    '12345678901',
                    'rogerio@felix.net',
                    '86-99818-1818',
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
