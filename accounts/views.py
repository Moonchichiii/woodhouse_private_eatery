from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login ,logout
from django.contrib import messages
from django.conf import settings


# Create your views here.

def signup_view(request):
    # Signup view, once signed up, the user is redirected to the bookig dashboard
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('bookings:booking_dashboard')
            
    else:
        form = UserCreationForm()
        context = {
        'form': form,
        'GOOGLE_API_KEY': settings.GOOGLE_API_KEY
        }
    return render(request, 'registration/signup.html', context)

 

def login_view(request):    
    # Shared login / for  guests and staff
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_superuser:
                return redirect('/admin/')
            else:
                return redirect('bookings:booking_dashboard')
        else:
            messages.error(request, 'Wrong username or password.')
    else:
        form = AuthenticationForm()
        context = {
        'form': form,
        'GOOGLE_API_KEY': settings.GOOGLE_API_KEY
        }
    return render(request, 'registration/login.html', context)




def Logout_View(request):    
    # Standard django Logout / with a different redirect
    logout(request)
    context = {        
        'GOOGLE_API_KEY': settings.GOOGLE_API_KEY
        }
    return render(request, 'registration/logout.html', context)



    