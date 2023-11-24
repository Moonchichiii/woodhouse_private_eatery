from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from . views import signup_view, login_view


UserModel = get_user_model()

class SignUpTests(TestCase):

    def setUp(self):
        
        self.user_data = {
            'username': 'nilsson', 
            'password1': 'testtesttest',
            'password2': 'testtesttest',
        }        
        
        self.signup_url = reverse('accounts:signup')
        self.login_url = reverse('accounts:login')

    def test_signup_view(self):        
        response = self.client.post(self.signup_url, self.user_data)
        self.assertTrue(UserModel.objects.filter(username='nilsson').exists())
        self.assertRedirects(response, reverse('bookings:booking_dashboard'))
        

    def test_login_view(self):        
        response = self.client.post(self.signup_url, self.user_data)
        self.assertTrue(UserModel.objects.filter(username='nilsson').exists())
        self.assertRedirects(response, reverse('bookings:booking_dashboard'))
    
       
        

  