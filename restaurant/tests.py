from django.test import TestCase
from rest_framework import status

from .models import Menu, Booking
from .serializers import MenuSerializer
from rest_framework.test import APIClient
from .views import MenuViewSet, BookingViewSet


# Create your tests here.


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Chicken", price=200, description="Description")
        self.assertEqual(item.title, "Chicken")


class BookingItemTest(TestCase):
    def test_get_item(self):
        item = Booking.objects.create(name="Mr. X", reservation_date="2023-12-30", no_of_guests=2)
        self.assertEqual(item.reservation_date, "2023-12-30")


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