from django.contrib import admin
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls', namespace='frontend')), 
    path('accounts/', include('accounts.urls', namespace='accounts')), 
    path('bookings/', include('bookings.urls', namespace='bookings')), 
    path('menu/', include('menu.urls', namespace='menu')), 
]
