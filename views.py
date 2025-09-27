from rest_framework import generics
from .models import UserReview
from .serializers import UserReviewSerializer

class UserReviewCreateView(generics.CreateAPIView):
    queryset = UserReview.objects.all()
    serializers_class = UserReviewSerializer

class MenuItemReviewListView(generics.ListAPIView):
    serializer_class = UserReviewSerializer

    def get_queryset(self):
        menu_item_id = self.request.query_params.get('menu_item')
        return UserReview.objects.filter(menu_item__id=menu_item_id)
        