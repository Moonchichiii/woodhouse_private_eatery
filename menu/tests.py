from django.test import TestCase
from .views import menu_view, recipe_view, gallery_view
from . models import Menu


# Create your tests here.

class MenuCreate(TestCase):

    def test_menu_create(self):
        
        
        menu_item = Menu.objects.create(
            name="Fish soup",
            category=Menu.STARTER,
            price=20
        )
        
        self.assertEqual(menu_item.name, "Fish soup")

        self.assertEqual(menu_item.category, Menu.STARTER)

        self.assertEqual(menu_item.price, 20)


def test_menu_view(self):
        response = self.client.get(reverse('menu_view'))

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'menu.html')

def test_recipe_view(self):
        response = self.client.get(reverse('gallery_view'))

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'gallery.html')


def test_recipe_view(self):
        response = self.client.get(reverse('recipe_view'))

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'recipes.html')