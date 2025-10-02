from rest_framework import serializer
from.models import Table

class TableSerializer(serializers.modelSerializer):
    class Meta:
        model = Table 
        fields = ['table_number','capacity','is_available']