from http import HTTPStatus
from datetime import timedelta


from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now


from users.forms import User_Register_Form
from .models import User, Email_Verification

class User_Registration_View_TestCase(TestCase):

    def setUp(self):
        self.path = reverse('users:register')
        self.data = {
            'first_name': 'Fedor', 'last_name': 'Miasnikov',
            'username': 'fedosil', 'email': 'fedosil@yandex.ru',
            'password1': '123456pP', 'password2': '123456pP',
        }

    def test_registration_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store - Регистрация')
        self.assertTemplateUsed(response, 'users/register.html')

    def test_registration_post_succes(self):
        username = self.data['username']
        self.assertFalse(User.objects.filter(username=username).exists())
        response = self.client.post(self.path, self.data)

        # creating of user
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('users:login'))
        self.assertTrue(User.objects.filter(username=username).exists())

        # creating email verification
        email_verification = Email_Verification.objects.filter(user__username=username)
        self.assertTrue(email_verification.exists())
        self.assertEqual(
            email_verification.first().expiration.date(),
            (now() + timedelta(hours=48)).date()
        )

    def test_registration_post_error(self):
        User.objects.create(username=self.data['username'])
        response = self.client.post(self.path, self.data)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Пользователь с таким именем уже существует.', html=True)