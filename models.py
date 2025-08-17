from django.db import models 
from django.contrib.auth.models import User

class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    Price = models.DecimalField(max_digits=6, decimal_places=2)


    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending',' Pending'),
        ('confirmed', ' Confirmed'),
        ('delivered', ' Delivered'),
        ('cancelled', 'Cancelled'),

    ]

    customer =models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    item =  models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="orders")
    quantity = models.PositiveIntegerField(default=1)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=20, choices = STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args,**kwargs):
        self.total_amount = self.item.price * self.quantity
        super().save(*args,**kwargs)

    def __str__(self):
        return f"Order #{self.id} by {self.customer.username} - {self.status}"