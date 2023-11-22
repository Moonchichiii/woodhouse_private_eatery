from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
 
    path('booking_dashboard/', views.booking_dashboard_view, name='booking_dashboard'),     
    path('make_booking/', views.make_booking_view, name='make_booking'),
    path('edit_booking/<int:booking_id>/', views.edit_booking_view, name='edit_booking'),     
    path('confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
    path('cancel/<int:booking_id>/', views.cancel_booking_view, name='cancel_booking'),
    
]