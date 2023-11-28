from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Bookings  
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
            'time_slot': 2,  
            'first_name': 'user',
            'last_name': 'user',
            'email': 'user@gmail.com',
            'phone_number': '436463463456',
            'allergy': 'none',
        }

    def test_past_booking_date(self):

        past_date = timezone.localdate() - timedelta(days=1)
        self.form_data['date'] = past_date.strftime('%Y-%m-%d')
        
        form = BookingsForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        
        


    def test_invalid_booking_slot(self):
        self.form_data['time_slot'] = 12
    
        form = BookingsForm(data=self.form_data)
    
        self.assertFalse(form.is_valid())
        self.assertIn('time_slot', form.errors)


        
    def test_valid_future_booking_time(self):
        future_date = timezone.localdate() + timedelta(days=1)

        self.form_data['date'] = future_date.strftime('%Y-%m-%d')

        form = BookingsForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        
        


    