from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime
from django.utils import timezone
from . models import Bookings




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


    def __init__(self, *args, **kwargs):
        super(BookingsForm, self).__init__(*args, **kwargs)
        self.fields['time'].choices = Bookings.TIME_OPTIONS


    def clean_date(self):
        # checking if the date is in the past
        booking_date = self.cleaned_data.get("date")
        if not booking_date:
            raise ValidationError("Booking date is required")

        if booking_date < timezone.localdate():
            raise ValidationError("Date has past, try again")

        return booking_date


    def clean_time(self):
        # checking if time has passed
        booking_time = self.cleaned_data.get("time")
        if not booking_time:
            raise ValidationError("Booking time is required")

        booking_time_str = booking_time.strftime("%H:%M")
        valid_times = [time_val[0] for time_val in self.fields['time'].choices]

        if booking_time_str not in valid_times:
            raise ValidationError("Time has past already, try again!")

        return booking_time


    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['date'] = self.clean_date()
        cleaned_data['time'] = self.clean_time()

        number_of_guests = cleaned_data.get("number_of_guests", 0)
        max_guests = 20

        booking_date = cleaned_data['date']
        booking_time = cleaned_data['time']


        # Check if the booking exceeds the maximum number of guests
        existing_bookings_count = Bookings.objects.filter(
            date=booking_date, time=booking_time
        ).aggregate(total_guests=models.Sum('number_of_guests'))['total_guests'] or 0

        if existing_bookings_count + number_of_guests > max_guests:
            raise ValidationError("Sorry, fully booked! Please choose another time or date")

        return cleaned_data