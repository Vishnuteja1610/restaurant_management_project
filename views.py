from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from .models import MenuItem
from .serializers import MenuItemSerializer

class UpdateMenuItemView(APIView):
    permission_classes=[permissions.IsAdminUser]

    def put(self, request, pk):
        menu_item = get_object_or_404(MenuItem, pk=pk)
        serializers = MenuItemSerializer(menu_item,data=request.data,partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        