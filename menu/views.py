from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from . models import Menu

# Create your views here.


def menu_view(request):
    """ Getting the menu from the db, and displaying it """
    
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
     return render(request,'recipes.html')


def gallery_view(request):
     return render(request,'gallery.html')



