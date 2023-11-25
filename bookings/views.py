from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import BookingsForm
from .models import Bookings
from django.conf import settings



# Create your views here.


@login_required
def booking_dashboard_view(request):
    """ Access only for logged in users """
    context = {'GOOGLE_API_KEY': settings.GOOGLE_API_KEY}
    user_bookings = Bookings.objects.filter(user=request.user)
    return render(request, 'bookings/booking_dashboard.html', {'bookings': user_bookings}, context)


    
def make_booking_view(request):
    """ Checking for submission, using the BookingForm,  """
    context = {'GOOGLE_API_KEY': settings.GOOGLE_API_KEY}
    if request.method == 'POST':
        form = BookingsForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('bookings:booking_confirmation', booking_id=booking.id)            
    else:
        form = BookingsForm()
    return render(request, 'bookings/make_booking_form.html', {'form': form}, context)





@login_required
def booking_confirmation(request, booking_id):
    """ Passing the booking_id to user that is logged in, and displays it """
    booking = get_object_or_404(Bookings, id=booking_id, user=request.user)
    return render(request, 'bookings/booking_confirmation.html', {'booking': booking})



    
@login_required
def edit_booking_view(request, booking_id):
    context = {'GOOGLE_API_KEY': settings.GOOGLE_API_KEY}
    """ Allows logged in users to edit booking based on booking_id  """
    booking = get_object_or_404(Bookings, id=booking_id, user=request.user)
    if request.method == 'POST':
        form = BookingsForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('bookings:booking_dashboard')
    else:
        form = BookingsForm(instance=booking)
    return render(request, 'bookings/edit_booking.html', {'form': form, 'booking': booking}, context)
   



@login_required
def cancel_booking_view(request, booking_id):
    """ Deletes the booking based on the booking_id  and logged in user.  """
    context = {'GOOGLE_API_KEY': settings.GOOGLE_API_KEY}
    booking = get_object_or_404(Bookings, id=booking_id, user=request.user)
    booking.delete()  
    return redirect('bookings:booking_dashboard', context)







 
 
    