from django.urls import path
from .views import MenuItemsByCategoryView

urlpatterns = [
    path('menu-items/', MenuItemsByCategoryView.as_view(),name='menu-items-by-category'),
]