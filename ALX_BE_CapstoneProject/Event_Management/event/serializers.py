from rest_framework import serializers
from .models import (
                     Event)

#User = get_user_model


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__' 