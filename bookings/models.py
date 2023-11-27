from django.db import models
from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta, time
from django.conf import settings

# Create your models here.


class Bookings(models.Model):
    
    GUEST_OPTIONS = [(i,str(i)) for i in range(1, 11)]

    TIME_OPTIONS = [
        ("17:00", "17:00"),
        ("17:30", "17:30"),
        ("18:00", "18:00"),
        ("18:30", "18:30"),
        ("19:00", "19:00"),
        ("19:30", "19:30"),
        ("20:00", "20:00"),
        ("20:30", "20:30"),
        ("21:00", "21:00"),
        ("21:30", "21:30"),        
        ("22:00", "22:00"),
    ]

       
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings', null=True, blank=True)
    number_of_guests = models.PositiveIntegerField(choices=GUEST_OPTIONS)
    date = models.DateField()
    time = models.TimeField(choices=TIME_OPTIONS)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)    
    email = models.EmailField(max_length=50, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False) 
    allergy = models.TextField(max_length=20,blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.date} {self.time}"