from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class EventOperationsMixin:
    def list_events(self, request):
        events = self.get_queryset()
        filters = self.get_filters(request.query_params)

        for filter_key, filter_value in filters.items():
            if filter_value is not None:
                events = events.filter(**filter_value)

        page = self.paginate_queryset(events)
        serializer = self.get_serializer(page, many=True) if page is not None else self.get_serializer(events, many=True)
        return self.get_paginated_response(serializer.data) if page is not None else Response(serializer.data)

    def create_event(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['organizer'] = request.user
            event = serializer.save()
            return Response({'message': 'Event created', 'event': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update_event(self, request, pk=None):
        event = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(event, data=request.data, partial=True)
        if serializer.is_valid():
            self.check_object_permissions(request, event)
            updated_event = serializer.save()
            return Response({'message': 'Event updated', 'event': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy_event(self, request, pk=None):
        event = get_object_or_404(self.get_queryset(), pk=pk)
        self.check_object_permissions(request, event)
        event.delete()
        return Response({'message': 'Event deleted'}, status=status.HTTP_204_NO_CONTENT)
