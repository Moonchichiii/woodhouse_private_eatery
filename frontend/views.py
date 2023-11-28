from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse


# Create your views here.




def index(request):
    # Getting the maps api key, from settings / rendering the landingpage
    context = {'GOOGLE_API_KEY': settings.GOOGLE_API_KEY}
    return render(request, 'index.html', context)


def base(request):
    context = {'GOOGLE_API_KEY': settings.GOOGLE_API_KEY}
    return render(request, 'base.html', context)

def terms(request):
     return render(request,'terms.html')


def privacy(request):
     return render(request,'privacy.html')



