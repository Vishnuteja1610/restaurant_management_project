from django.contrib import admin 
from .models import ContractSubmission

@admin.regsiter(ContractSubmission)
class ContractSubmissionAdmin(admin.ModelAdmin):
    list_display = ("name","email","submitted_at")