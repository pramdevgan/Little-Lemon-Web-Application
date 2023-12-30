from django.db import models


# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=100)
    reservation_date = models.DateField()
    no_of_guests = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Menu(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='menu_images', null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.price}"

