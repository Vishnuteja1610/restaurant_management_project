from rest_framework.generics import ListAPIView
from .models import MenuItem
from .serializers import MenuItemSerializer

class DailySpecialsView(ListAPIView):
    queryset = MenuItem.objects.filter(is_daily_special=True)
    serializer_class=MenuItemSerializer
    