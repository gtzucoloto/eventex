from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def test_form_has_fields(self):
        """Form must have 4 fields"""
        form = SubscriptionForm()
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_cpf_is_digit(self):
        """CPF must only accpet digits"""
        form = self.make_valideted_form(cpf='ABCD5678901')
        self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_have_11_digits(self):
        """CPF must have 11 digits"""
        form = self.make_valideted_form(cpf='1234')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def test_must_be_capitalized(self):
        """Name must be capitalized"""
        form = self.make_valideted_form(name='GABRIEL zucoloto')
        self.assertEqual('Gabriel Zucoloto', form.cleaned_data['name'])

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        execption = errors_list[0]
        self.assertEqual(code, execption.code)

    def make_valideted_form(self, **kwargs):
        valid = dict(name='Gabriel Zucoloto', cpf='12345678901',
                     email='gtzucoloto@gmail.com', phone='27-995101402')

        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form
