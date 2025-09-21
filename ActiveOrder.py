from django.db import models

class ActiveOrderManager(models.Manager):
    def get_active_orders(self):
        return self.get_queryset().filter(status__in=['pending','processing'])

class Order(models.Model):
    status = models.CharField(max_length=20)

    objects = ActiveOrderManager()
    