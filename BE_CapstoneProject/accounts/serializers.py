from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile, CustomUser

class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)

    class Meta:
        model = CustomUser
        fields = ('username', 'email',  'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__' 