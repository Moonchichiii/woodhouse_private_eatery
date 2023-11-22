from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


# Create your views here.

def signup_view(request):
    """
    Signup view, once signed up, the user is redirected to the booking dashboard.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('bookings:booking_dashboard')
            
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})