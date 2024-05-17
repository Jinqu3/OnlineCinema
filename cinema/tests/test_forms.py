from django.test import TestCase
from django.urls import resolve,reverse
from users.forms import RegisterForm,LoginForm

class TestForms(TestCase):

    def test_register_form_valid_data(self):
        form = RegisterForm(data={
            'username' : 'username',
            'password1' : 'password', 
            'password2' : 'password',
            'email':'email',
            'name': 'name',
            'surname':'surname',
            'lastname':'lastname'
        })

        self.assertTrue(form.is_valid())

    def test_register_form_has_no_data(self):
        form = RegisterForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),7)

    def test_login_form_valid_data(self):
        form = LoginForm(data={
            "username" : 'username',
            'password' : 'password', 
        })

        self.assertTrue(form.is_valid())

    def test_login_form_has_no_data(self):
        form = LoginForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),2)