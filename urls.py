from django.urls import path
from .views import menu_api
from . import views 


urlpatterns = [
    path('api/menu/',menu_api, name='menu_api'),
    path('',views.home, name='home'),
    path('faq/', views.faq,name='faq'),
]
