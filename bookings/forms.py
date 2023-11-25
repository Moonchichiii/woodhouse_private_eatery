from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from . models import Bookings
from django.db import models


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
            'number_of_guests = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 20})),
            
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'type': 'tel'}),           
            'time = forms.ChoiceField(choices=Bookings.TIME_OPTIONS, widget=forms.Select(attrs={'class': 'form-control'})),
            'date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})),
            'allergy = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'class': 'form-control'})),
        }

    
    def clean(self):
        cleaned_data = super()






    def clean_date(self):
        date = self.cleaned_data.get("date")
        if date and date < timezone.localdate():
            raise ValidationError("Date has passed already.")
        return date

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        time = cleaned_data.get("time")
        number_of_guests = cleaned_data.get("number_of_guests", 0)

        if date and time:
            self.check_booking(date, time, number_of_guests)

        return cleaned_data




    def check_booking(self, date, time, number_of_guests):
        max_guests = 20
        existing_bookings_count = Bookings.objects.filter(date=date, time=time).aggregate(
            total_guests=models.Sum('number_of_guests')
        )['total_guests'] or 0

        if existing_bookings_count + number_of_guests > max_guests:
            raise ValidationError(
                "Sorry fully booked! Please choose time or date")