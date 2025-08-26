from django.contrib import admin
from .models import ResturantLocation

@admin.register(ResturantLocation)
class ResturantLocationAdmin(admin.ModelAdmin):
    list_display = ("address","city","state","zip_code")
    search_fields = ("city","state","zip_code")