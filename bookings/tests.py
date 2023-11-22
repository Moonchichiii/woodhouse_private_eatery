from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.

class LoginRequiredTest(TestCase):

    def test_login_required_redirect(self):

        login_required = reverse('bookings:booking_dashboard')       

        response = self.client.get(login_required)        

        self.assertEqual(response.status_code, 302)