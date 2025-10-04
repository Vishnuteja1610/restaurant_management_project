from rest_framework import viewsets
from .models import MenuCategory
from .serializers import MenuCategorySerializer

class MenuCategoryViewSet(viewsets.ModelViewSet):
    querryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer