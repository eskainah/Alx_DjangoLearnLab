from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

from .models import CustomUser
from .serializers import CustomUser_Serializer, UserRegistration_Serializer
# Create your views here.
class RegisterView(CreateAPIView):
    permission_classes = (AllowAny,)

    queryset = CustomUser.objects.all()
    serializer_class = UserRegistration_Serializer

    def post(self, request):
        serializer = UserRegistration_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if not user:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
