from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .serializer import SignupSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "message": "User registered successfully",
            "username": user.username,
            "role": user.role,
            "token": token.key
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "message": "Login successful",
            "username": user.username,
            "role": user.role,
            "token": token.key
        })
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard(request):
    try:
        # Check if user has 'role' attribute
        if not hasattr(request.user, 'role'):
            return Response(
                {"error": "User role not found. Please contact the administrator."},
                status=status.HTTP_400_BAD_REQUEST
            )


        role = request.user.role

        # Dashboard data based on role
        if role == 'admin':
            data = {'dashboard': 'Admin Dashboard Data'}
        elif role == 'superadmin':
            data = {'dashboard': 'SuperAdmin Dashboard Data'}
        else:
            data = {'dashboard': 'User Dashboard Data'}

        return Response(data, status=status.HTTP_200_OK)

    except Exception as e:
        # Catch any unexpected error
        return Response(
            {"error": f"An unexpected error occurred: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

