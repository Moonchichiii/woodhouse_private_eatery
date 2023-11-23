from django.shortcuts import render, redirect, get_object_or_404, HttpResponse

# Create your views here.


def menu_view(request):
     return render(request,'menu.html')


def recipe_view(request):
     return render(request,'recipes.html')


def gallery_view(request):
     return render(request,'gallery.html')



