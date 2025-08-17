from django.contrib import admin
from .models import Menu, Order

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name','price','description')
    search_field = ('name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name','item','quantity','created_at')
    list_filter = ('created_at','item')
    search_fields = ('customer_name',)