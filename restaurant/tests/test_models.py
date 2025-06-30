from django.test import TestCase
from restaurant import models


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = models.MenuItem.objects.create(title="IceCream", price=4, inventory=100)
        self.assertEqual(item.get_item(), "IceCream : 4")