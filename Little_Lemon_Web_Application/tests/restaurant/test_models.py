from unittest import TestCase

from restaurant.models import Menu, Booking


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Chicken", price=200, description="Description")
        self.assertEqual(item.title, "Chicken")


class BookingItemTest(TestCase):
    def test_get_item(self):
        item = Booking.objects.create(name="Mr. X", reservation_date="2023-12-30", no_of_guests=2)
        self.assertEqual(item.reservation_date, "2023-12-30")
