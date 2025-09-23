from decimal import Decimal
from django.db import models

class Order(models.Model):

    def calculate_total(self):
        total = Decimal('0.00')
        for item in self.orderitem_set.all():
            total += item.price * item.quantity
        return total

class OrderItem(models.Model):
    Order=models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey('home.MenuItem', on_delete= models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

class MenuItem(models.Model):
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    