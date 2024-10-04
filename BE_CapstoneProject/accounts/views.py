
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import UserSerializer, ProfileSerializer
from .models import Profile, CustomUser
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

class CustomAuthToken(ObtainAuthToken):
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

class AuthViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    def create(self, request):  # For registration
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            Token.objects.create(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'], url_path='login')
    def login(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'message': 'Login successful'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid Credentials', 'message': 'Please check username or password'}, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['post'], url_path='logout')
    def logout(self, request):
        if request.user.is_authenticated:
            request.user.auth_token.delete()
            return Response({'message': 'Logout successful'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'User is not logged in'}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'], permission_classes = [IsAuthenticated], url_path='profile')
    
    def user_profile(self, request):
        if request.user.is_authenticated:
            try:
                profile = request.user.profile
                serializer = ProfileSerializer(profile)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Profile.DoesNotExist:
                return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error': 'User is not logged in'}, status=status.HTTP_401_UNAUTHORIZED)
    
     #allow only authenticated users can update their profile
    @action(detail=False, methods=['put'], permission_classes = [IsAuthenticated], url_path='update_profile')
    def update_profile(self, request):
        profile = request.user.profile
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # allow only authenticated users can delete their profile
    @action(detail=False, methods=['delete'], permission_classes = [IsAuthenticated], url_path='delete_profile')
 
    def delete_profile(self, request):
        try:
            profile = request.user.profile
            profile.delete()
            request.user.delete()
            return Response({'message': 'Profile deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Profile.DoesNotExist:
            return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)
            