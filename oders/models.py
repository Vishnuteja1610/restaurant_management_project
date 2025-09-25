from django.db import models

class OrderManager(models.Manager):
    def by_status(self, status):
        return self.filter(status=status)

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending','Pending'),
        ('processing','Processing'),
        ('cancelled','Cancelled'),
        ('completed','Completed'),

    ]
    status = models.CharField(max_length=20,choices=STATUS_CHOICES, default='pending')

    objects=OrderManager()