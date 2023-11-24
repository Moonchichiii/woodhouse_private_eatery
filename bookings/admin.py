from django.contrib import admin
from . models import Bookings

# Register your models here.
@admin.register(Bookings)
class BookingManager(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name', 
        'date', 
        'time',
        'number_of_guests',
        'phone_number',
        'email','allergy'
        )

    search_fields = (
        'first_name',
        'last_name',
        'email', 
        'phone_number'
        )
    
    list_filter = (
        'date',
        'time',
        'number_of_guests'
        )   