from django.db import models

# Create your models here.
class Menu(models.Model):

    STARTER = 'Starter'
    MAIN_COURSE = 'Main Couse'
    DESSERT = 'Dessert'

 
    CATEGORY_OPTIONS = [
        (STARTER, 'Starter'),
        (MAIN_COURSE, 'Main Course'),
        (DESSERT, 'Dessert'),
    ]
    
    name = models.CharField(max_length=180,)
    category = models.CharField(max_length=80, choices=CATEGORY_OPTIONS)
    price = models.DecimalField(max_digits=6, decimal_places=2)