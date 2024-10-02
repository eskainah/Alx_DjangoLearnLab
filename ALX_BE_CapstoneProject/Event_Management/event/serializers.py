from rest_framework import serializers
from .models import (Profile,
                     Event)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'business_name']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__' 