from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as drf_status
from .models import Order

class OrderStatusUpdateView(APIView):
    def post(self, request):
        order_id = request.data.get('order_id')
        new_status = request.data.get('status')
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response({'error':'Order not found. '}, status=drf_status.HTTP_404_NOT_FOUND)
        allowed_statuses = dict(Order.STATUS_CHOICES).keys()
        if new_status not in allowed_statuses:
            return Response({'error':'Invalid status.'}, status = drf_status.HTTP_400_BAD_REQUEST)
        order.status = new_status
        order.save()
        return Response({'message':'Order status updated.', 'order_id':order_id, 'new_status':new_status})