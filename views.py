from rest_framework import generics
from .models import Restaurant
from .serializers import RestaurantSerializer

class RestaurantInfoView(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get_object(self):
        return Restaurant.objects.first()
        