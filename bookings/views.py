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
    if request.method == 'POST':
        form = BookingsForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('bookings:booking_confirmation', booking_id=booking.id)            
    else:
        form = BookingsForm()
    return render(request, 'make_booking_form.html', {'form': form})

    
@login_required
def edit_booking_view(request, booking_id):
    booking = get_object_or_404(Bookings, id=booking_id, user=request.user)
    if request.method == 'POST':
        form = BookingsForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('bookings:booking_dashboard')
    else:
        form = BookingsForm(instance=booking)
    return render(request, 'edit_booking.html', {'form': form, 'booking': booking})
   


@login_required
def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Bookings, id=booking_id, user=request.user)
    return render(request, 'booking_confirmation.html', {'booking': booking})



@login_required
def cancel_booking_view(request, booking_id):
    booking = get_object_or_404(Bookings, id=booking_id, user=request.user)
    booking.delete()  
    return redirect('bookings:booking_dashboard')







 
 
    