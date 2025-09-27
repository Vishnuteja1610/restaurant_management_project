from rest_framework import serializers
from .models import Order

class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','status']
    
    def validate_status(self,value):
        allowed = dict(Order.STATUS_CHOICES).keys()
        if value not in allowed:
            raise serializers.ValidationError("Invalid status.")
        return value
        