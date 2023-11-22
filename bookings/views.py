from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import BookingsForm
from .models import Bookings



# Create your views here.


@login_required
def booking_dashboard_view(request):        
    user_bookings = Bookings.objects.filter(user=request.user)
    return render(request, 'bookings/booking_dashboard.html', {'bookings': user_bookings})


    
def make_booking_view(request):
    pass

    

def edit_booking_view(request, booking_id):
    pass


def booking_confirmation(request):
    pass


def cancel_booking_view(request):
    pass







 
 
    