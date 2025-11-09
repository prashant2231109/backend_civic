from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import status
from .models import Report
from .serializers import ReportSerializer

# @api_view(['POST'])
# @permission_classes([AllowAny])
# def create_report(request):
#     serializer = ReportSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save(user=request.user)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_report(request):
    try:
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            # Save without user for anonymous reports
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        return Response(
            {"error": f"An error occurred: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_reports(request):
    try:
        # Check if user has role attribute
        if not hasattr(request.user, 'role'):
            return Response(
                {"error": "User role not found"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if request.user.role in ['admin', 'superadmin']:
            reports = Report.objects.all()
        else:
            reports = Report.objects.filter(user=request.user)
        
        serializer = ReportSerializer(reports, many=True)
        return Response(serializer.data)
    
    except Exception as e:
        return Response(
            {"error": f"An error occurred: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
