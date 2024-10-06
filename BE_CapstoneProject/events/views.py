from rest_framework import viewsets, permissions
from django.utils import timezone
from .models import Event
from .serializers import EventSerializer
from .permissions import IsEventOwner
from dateutil import parser
from .mixins import EventOperationsMixin
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class EventViewSet(viewsets.ModelViewSet, EventOperationsMixin):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsEventOwner]

    def get_queryset(self):
        now = timezone.now()
        return Event.objects.filter(date_time__gt=now)

    def list(self, request):
        return self.list_events(request)

    def create(self, request):
        return self.create_event(request)

    def update(self, request, pk=None):
        return self.update_event(request, pk)

    def destroy(self, request, pk=None):
        return self.destroy_event(request, pk)

    def get_filters(self, query_params):
        filters = {}
        if query_params.get('title'):
            filters['title__icontains'] = query_params['title']
        if query_params.get('location'):
            filters['location__icontains'] = query_params['location']
        if start_date := query_params.get('start_date'):
            filters['date_time__gte'] = self.parse_date(start_date)
        if end_date := query_params.get('end_date'):
            filters['date_time__lte'] = self.parse_date(end_date)
        return filters

    def parse_date(self, date_str):
        try:
            return parser.parse(date_str)
        except (ValueError, TypeError):
            raise Response({'error': f'Invalid date format for {date_str}'}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        event = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(event)
        return Response(serializer.data)