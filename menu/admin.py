from django.contrib import admin
from . models import Menu

# Register your models here.
@admin.register(Menu)
class MenuManager(admin.ModelAdmin):
    list_display = ('name', 'category')
    