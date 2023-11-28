from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from . models import Menu
from django.conf import settings

# Create your views here.


def menu_view(request):
    # Getting the menu from the db, and displaying it
    
    STARTER = 'Starter'
    MAIN_COURSE = 'Main Course'  
    DESSERT = 'Dessert'

    starters = Menu.objects.filter(category=STARTER)
    main_courses = Menu.objects.filter(category=MAIN_COURSE)
    desserts = Menu.objects.filter(category=DESSERT)

    context = {        
        'starters': starters, 
        'main_courses': main_courses, 
        'desserts': desserts
        }

    return render(request, 'menu.html', context)


def recipe_view(request):
    
    # Renders the recipe page
    return render(request,'recipes.html',{'hide_map': True})


def gallery_view(request):
    # Renderes Modal Gallery
    return render(request,'gallery.html',{'hide_map': True})



