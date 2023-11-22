from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views  

# Create your views here.

app_name = 'frontend'


urlpatterns = [

 path('', views.index, name='index'),

]