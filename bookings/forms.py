from datetime import datetime, time
from django.db import models
from django import forms
from django.core.exceptions import ValidationError
from .models import Bookings



class BookingsForm(forms.ModelForm):

    class Meta:
        model = Bookings
        fields = [           
            'number_of_guests',
            'date',
            'time_slot',  
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'allergy'
        ]
        

        widgets = {
            'number_of_guests': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 20}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time_slot': forms.Select(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'type': 'tel'}),
            'allergy': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }


    def clean(self):
        # checks all fields, including the max_guests that day,date not in the past.   
        cleaned_data = super().clean()
        booking_date = cleaned_data.get('date')
        booking_time_slot = cleaned_data.get('time_slot')
        number_of_guests = cleaned_data.get('number_of_guests')
        max_guests = 20
        now = datetime.now()

        
        # checking if the date is in the past
        if booking_date and booking_date < now.date():
            raise ValidationError("Booking date cannot be in the past.")

        

        return cleaned_data

        # Check if the booking exceeds the maximum number of guests
        existing_bookings_count = Bookings.objects.filter(
            date=booking_date, time=booking_time
        ).aggregate(total_guests=models.Sum('number_of_guests'))['total_guests'] or 0

        

        if existing_bookings_count + number_of_guests > max_guests:
            raise ValidationError("Sorry, fully booked! Please choose another time or date.")

        return cleaned_data