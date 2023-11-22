from django.test import TestCase
from django.urls import reverse

# Create your tests here.



class ViewTest(TestCase):

    def test_index_view(self):
        path = reverse('frontend:index')                
        response = self.client.get(path)        
        self.assertEqual(response.status_code, 200)