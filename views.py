from rest_framework.views import APIView
from rest_framework.response import response
from rest_framework import status
from .models import Coupon
from django.utils import timezone

class CouponValidationview(APIView):
    def post(self, request):
        code = request.data.get('code')
        if not code:
            return response({'error': 'code is required' },status=status.HTTP_400_BAD_REQUEST)