from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime
from . models import Bookings
from django.db import models
from django.utils import timezone



class BookingsForm(forms.ModelForm):

    class Meta:
        model = Bookings
        fields = [
            'number_of_guests',
            'date',
            'time',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'allergy'
        ]

        widgets = {

            'number_of_guests': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 20}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.Select(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'type': 'tel'}),
            'allergy': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),

        }

    def clean_date(self):
        # checking so it's not possible to book past current date,         
        date = self.cleaned_data.get("date")
        if date and date < timezone.localdate():
            raise ValidationError("Date has passed, try again .")
        return date


    def clean_time(self):
    # checking that the time has not passed and within the time options limits, set in the models.
        booking_time = self.cleaned_data.get("time")
        date = self.cleaned_data.get("date")

        if date and date < timezone.localdate():
            raise ValidationError("Can't book in the past!")

        if not (time(18, 0) <= booking_time < time(22, 0)):
            raise ValidationError("Booking hours are between 18:00 & 22:00,")

        return booking_time


    def clean(self):
        # checking that it's returning both date and time  
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        time = cleaned_data.get("time")
        number_of_guests = cleaned_data.get("number_of_guests", 0)
        
        
        max_guests = 20


        if date and time:
            # check if total number of guests if there is already reached on that date and time.
            existing_bookings_count = Bookings.objects.filter(date=date, time=time).aggregate(
                total_guests=models.Sum('number_of_guests')
            )['total_guests'] or 0

            if existing_bookings_count + number_of_guests > max_guests:
                # checking current booking exceeds the maximum guest limit 
                raise ValidationError("Sorry, fully booked! Please choose another time or date")

        return cleaned_data
