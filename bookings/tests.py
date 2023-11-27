from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from django.utils import timezone
from datetime import timedelta
from .forms import BookingsForm

# Create your tests here.

class LoginRequiredTest(TestCase):

    def test_login_required_redirect(self):

        login_required = reverse('bookings:booking_dashboard')       

        response = self.client.get(login_required)        

        self.assertEqual(response.status_code, 302)



class BookingsTest(TestCase):

    def setUp(self):
        self.form_data = {
            'number_of_guests': 8,
            'date': '2023-11-28',  
            'time': '19:00',  
            'first_name': 'user',
            'last_name': 'user',
            'email': 'user@gmail.com',
            'phone_number': '436463463456',
            'allergy': 'none',
        }

    def test_past_booking_date_time(self):

        past_date = timezone.localdate() - timedelta(days=1)

        self.form_data['date'] = past_date.strftime('%Y-%m-%d') 

        form = BookingsForm(data=self.form_data)

        self.assertFalse(form.is_valid())

        self.assertIn('date', form.errors)

        self.assertIn("Date has past, try again", form.errors['date'])
