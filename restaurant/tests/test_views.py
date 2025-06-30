from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from restaurant import models, serializers
from rest_framework import status


class MenuViewTests(APITestCase):
    def setUp(self):
        # Create a test user for authenticated requests
        self.user = User.objects.create_user(username='testuser', password='testpassword123')

        # Create some initial Menu items
        self.menu1 = models.Menu.objects.create(title='Pizza Margherita', price='12.99', inventory=50)
        self.menu2 = models.Menu.objects.create(title='Spaghetti Carbonara', price='15.50', inventory=30)

        # URLs for Menu views
        self.menu_list_create_url = reverse('menu')
        print(self.menu_list_create_url)
        # Assumes URL name 'menu' for SingleMenuItemView (RetrieveUpdateDestroyAPIView)
        self.menu_detail_url = lambda pk: reverse('menu-item', kwargs={'pk': pk})
        print(self.menu_detail_url)
        print(self.menu1.pk)

    def test_get_all_menu_items_unauthenticated(self):
        response = self.client.get(self.menu_list_create_url)
        print(self.menu1.pk)
        print(response)
        print(response.data)

    def test_get_single_menu_items_unauthenticated(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.menu_detail_url(self.menu1.pk))
        print(self.client.get(self.menu_list_create_url))
        print(self.menu1.pk)
        print(response)
        print(response.data)
