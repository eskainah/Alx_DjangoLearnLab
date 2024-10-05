from rest_framework import serializers
from django.utils import timezone
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date_time', 'location', 'organizer', 'capacity', 'created_date']
    
    def validate(self, attrs):
        if 'date_time' in attrs and attrs['date_time'] < timezone.now():
            raise serializers.ValidationError("The event date and time must be in the future.")
        if 'title' not in attrs or not attrs['title']:
            raise serializers.ValidationError("Title is required.")
        if 'location' not in attrs or not attrs['location']:
            raise serializers.ValidationError("Location is required.")
        return attrs