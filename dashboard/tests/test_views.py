from django.test import TestCase
from dashboard.models import CustomUser
from django.urls import reverse


class LoginTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword')

    def test_login_successful(self):
        response = self.client.post(reverse('signin'), {'email': 'testuser@example.com', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.client.login(username='testuser@example.com', password='testpassword'))

    def test_login_unsuccessful(self):
        response = self.client.post(reverse('signin'), {'email': 'testuser@example.com', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200) 
        self.assertFalse(self.client.login(username='testuser@example.com', password='wrongpassword'))