from django.db import models
from .utils import calculate_discount

class Order(models.Model):

    def calculate_total(self):
        total=0
        for item in self.items.all():
            price = item.price
            discounted_price = calculate_discount(price, item)
            total +=discounted_price
        return total