from rest_framework import serializers
from django.utils import timezone
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date_time', 'location', 'capacity', 'current_capacity', 'created_date']
        read_only_fields = ['organizer']
        extra_kwargs = {
            'title': {'required': True}, 
            'location': {'required': True},  #Ensure title is require when creating an event
        }
        
    def validate(self, attrs):
        if 'date_time' in attrs and attrs['date_time'] < timezone.now():
            raise serializers.ValidationError("Please enter a date in the future")
        if 'title' in attrs and not attrs['title']:
            raise serializers.ValidationError("Title is required.")
        if 'location' in attrs and not attrs['location']:
            raise serializers.ValidationError("Location is required.")
        if attrs.get('current_capacity', 0) > attrs.get('capacity', 0):
            raise serializers.ValidationError("Current capacity cannot exceed maximum capacity.")
        return attrs
       
    