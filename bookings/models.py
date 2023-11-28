from django.db import models
from django.utils import timezone
from datetime import time
from django.conf import settings

# Create your models here.


class Bookings(models.Model):
    
    GUEST_OPTIONS = [(i,str(i)) for i in range(1, 11)]


    
    TIME_SLOTS = [
        (1, "13:00 - 15:00"),
        (2, "15:00 - 17:00"),
        (3, "17:00 - 19:00"),
        (4, "19:00 - 21:00"),
        (5, "21:00 - 22:00"),
        (6, "22:00 - 00:00"),
    ]       
       
       
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings', null=True, blank=True)
    number_of_guests = models.PositiveIntegerField(choices=GUEST_OPTIONS)
    date = models.DateField()
    time_slot = models.IntegerField(choices=TIME_SLOTS, default=1)
    timestamp_booking_made = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)    
    email = models.EmailField(max_length=50, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False) 
    allergy = models.TextField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.date} {self.get_time_slot_display()}"