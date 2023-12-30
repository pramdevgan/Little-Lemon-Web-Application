from unittest import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewSetTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.menu1 = Menu.objects.create(title="Pizza", price=200, description="Description")
        self.menu2 = Menu.objects.create(title="Tea", price=40, description="Description")

    def test_get_menu(self):
        response = self.client.get("/api/menu-items/")
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
