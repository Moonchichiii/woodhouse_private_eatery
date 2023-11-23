from django.urls import path, include
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from . import views

app_name = 'menu'

urlpatterns = [
    path('menu/', views.menu_view, name='menu'),
    path('recipe/', views.recipe_view, name='recipe'),
    path('gallery/', views.gallery_view, name='gallery'),
]