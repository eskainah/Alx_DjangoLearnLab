from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Profile

CustomUser = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=30, required=True)
    last_name = serializers.CharField(max_length=30, required=True)
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}, 'email': {'required': True}}

    def create(self, validated_data):
        #Handle profile data when provided
        profile_data = validated_data.pop('profile', None) 

        user = CustomUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        
        # Create profile 
        if profile_data:
            Profile.objects.create(user=user, **profile_data)
        return user
    
    #perform validation on username and email
    def validate_username(self, value):
        if CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username is already taken.")
        return value

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already registered.")
        return value
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__' 