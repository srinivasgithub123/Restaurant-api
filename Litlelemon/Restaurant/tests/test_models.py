from django.test import TestCase
from Restaurant.models import Menu  # Adjust the import based on your structure

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title="IceCream", Price=80.00, Inventory=100)
        self.assertEqual(str(item), "IceCream : 80.00")
