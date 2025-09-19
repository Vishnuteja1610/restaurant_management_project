from django.db.models.signals import post_save
from django.dispatch import reciver

def set_default_order_status(sender,instance,created, **kwargs):
    if created and instance.status is None:
        pending_status, _ = OrderStatus.objects.get_or_create(name="Pending")
        instance.status = pending_status
        instance.save()
        