from django.core import mail
from django.test.testcases import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Gabriel Zucoloto', cpf='12345678901',
                    email='gtzucoloto@gmail.com', phone='27-995101402')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'gtzucoloto@gmail.com'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['gtzucoloto@gmail.com', 'gtzucoloto@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = ("Gabriel Zucoloto",
                    "12345678901",
                    "gtzucoloto@gmail.com",
                    "27-995101402")
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
