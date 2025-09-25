from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as drf_status
from .models import Order

class CancelOrderView(APIView):
    def delete(self, request):
        order_id = request.data.get('order_id')

        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response({'error':'Order not found.'},status = drf_status.HTTP_404_NOT_FOUND)

        order.status = 'cancelled'
        order.save()
        return Response({'message':'Order cancelled.','order_id':order_id}, status=drf_status.HTTP_200_OK)
        