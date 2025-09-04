from django.urls import path
from . import views

urlpatterns = [
    path("",views.homepage, name="homepage")
    path("order/place/",views.place_order, name="place_order")
]