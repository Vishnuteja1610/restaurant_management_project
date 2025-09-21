from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemSearchView(APIView):
    def get(self,request):
        query = request.GET.get("q","")
        items = MenuItem.objects.filter(name__icontains= query)if query else MenuItem.objects.all()

        page_number = request.GET.get("page",1)
        paginator = paginator(items, 10)
        page_obj = paginator.get_page(page_number)

        serializer = MenuItemSerializer(page_obj, many=True)

        return Response({
            "count": paginator.count,
            "total_pages":paginator.num_pages,
            "current_page":page_obj.number,
            "results":serializer.data,
        } status=status.HTTP_200_OK)
        