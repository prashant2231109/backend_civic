# from rest_framework import serializers
# from .models import Report

# class ReportSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Report
#         fields = ['id', 'user', 'utility_type', 'location', 'gps_coordinates', 'description', 'photo', 'status', 'created_at']
#         read_only_fields = ['id', 'user', 'status', 'created_at']

from rest_framework import serializers
from .models import Report

class ReportSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Report
        fields = ['id', 'username', 'utility_type', 'location', 'gps_coordinates', 'description', 'photo', 'status', 'created_at']
        read_only_fields = ['id', 'username', 'status', 'created_at']
