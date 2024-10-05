from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Event
from .serializers import EventSerializer
from .permissions import IsEventOwner

# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated, IsEventOwner]

    def get_queryset(self):
        # Return events created by the authenticated user
        return Event.objects.filter(organizer=self.request.user)

    def list(self, request):
        events = self.get_queryset()  #returns user's events
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        event = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(event)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['organizer'] = request.user
            event = serializer.save()
            return Response(serializer.data, {'message': 'Event created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        event = get_object_or_404(self.get_queryset(), pk=pk) 
        serializer = self.get_serializer(event, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Event updated'}, serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        event = get_object_or_404(self.get_queryset(), pk=pk) 
        event.delete()
        return Response({'message': 'Event Deleted'}, status=status.HTTP_204_NO_CONTENT)