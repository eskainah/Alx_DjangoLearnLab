from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Event
from .serializers import EventSerializer
from .permissions import IsEventOwner
from django.utils import timezone

# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsEventOwner]  # Allow read-only for unauthenticated users

    def get_queryset(self):
        # Default to returning all upcoming events
        now = timezone.now()
        return Event.objects.filter(date_time__gt=now)

    def list(self, request):
        # Check for query parameters
        title = request.query_params.get('title', None)
        location = request.query_params.get('location', None)
        start_date = request.query_params.get('start_date', None)
        end_date = request.query_params.get('end_date', None)

        # Get the base queryset for upcoming events
        events = self.get_queryset()

        # Apply optional filters
        if title:
            events = events.filter(title__icontains=title)
        if location:
            events = events.filter(location__icontains=location)
        if start_date:
            events = events.filter(date_time__gte=start_date)
        if end_date:
            events = events.filter(date_time__lte=end_date)

        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)
    
    '''serializer_class = EventSerializer #list event creaete by user 
    permission_classes = [permissions.IsAuthenticated, IsEventOwner]

    def get_queryset(self):
        # Return events created by the authenticated user
        return Event.objects.filter(organizer=self.request.user)
    
    def list(self, request):
        events = self.get_queryset()  # Returns user's events
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)
'''
    def retrieve(self, request, pk=None):
        event = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(event)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Set the organizer to the current user
            serializer.validated_data['organizer'] = request.user
            event = serializer.save()
            return Response({'message': 'Event created', 'event': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk=None):
        event = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(event, data=request.data, partial=True)
        if serializer.is_valid():
            self.check_object_permissions(request, event) 
            updated_event = serializer.save()
            return Response({'message': 'Event updated', 'event': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        event = get_object_or_404(self.get_queryset(), pk=pk)
        self.check_object_permissions(request, event) 
        event.delete()
        return Response({'message': 'Event deleted'}, status=status.HTTP_204_NO_CONTENT)
