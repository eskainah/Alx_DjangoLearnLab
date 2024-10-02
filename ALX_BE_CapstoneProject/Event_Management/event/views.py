from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate

from event.forms import CustomUserCreationForm, EventForm
from django.contrib import messages

from .models import CustomUser, Event, Profile
from .serializers import ProfileSerializer, EventSerializer

from rest_framework import viewsets, permissions

from rest_framework.response import Response
from rest_framework import status

#render homepage
def home(request):
    return render(request, 'event/home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Login user after registration
            login(request, user)
            #Redirect to homepage
            return redirect('home')  
        else:
            messages.error(request, "There was an error with your registration.")
    else:
        #register the a new user
        form = CustomUserCreationForm()
    return render(request, 'event/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
             #Redirect to homepage
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'event/login.html')

#View for User profile
class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return the profile for the logged-in user
        return Profile.objects.filter(user=self.request.user)

    def create_profile(self, serializer):
        # Create a profile for the user
        serializer.save(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        # Override retrieve to return the profile of the logged-in user
        profile = get_object_or_404(Profile, user=request.user)
        serializer = self.get_serializer(profile)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        # Override update to allow users to update their own profile
        profile = get_object_or_404(Profile, user=request.user)
        serializer = self.get_serializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        # Override destroy to allow users to delete their own profile
        profile = get_object_or_404(Profile, user=request.user)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]  # Restrict access to authenticated users

    def list(self, request):
        """
        Retrieve a list of all events.
        """
        events = self.queryset
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Retrieve a specific event by ID.
        """
        try:
            event = self.get_object()
            serializer = self.get_serializer(event)
            return Response(serializer.data)
        except Event.DoesNotExist:
            messages.error(request, 'Event not found.')
            return redirect('event_list')  # Redirect to event list on error

    def create(self, request):
        """
        Create a new event.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            event = serializer.save()  # Save the event instance
            messages.success(request, 'Event created successfully!')
            return redirect('event_list')  # Redirect to the event list after creation
        else:
            messages.error(request, 'There was an error creating the event.')
            return render(request, 'events/event_form.html', {'form': serializer.errors})

    def update(self, request, pk=None):
        """
        Update an existing event by ID.
        """
        event = self.get_object()
        serializer = self.get_serializer(event, data=request.data, partial=True)  # Partial update
        if serializer.is_valid():
            serializer.save()  # Save the updated event instance
            messages.success(request, 'Event updated successfully!')
            return redirect('event_detail', pk=event.pk)  # Redirect to event detail after update
        else:
            messages.error(request, 'There was an error updating the event.')
            return render(request, 'events/event_form.html', {'form': serializer.errors})

    def destroy(self, request, pk=None):
        """
        Delete an existing event by ID.
        """
        event = self.get_object()
        event.delete()  # Delete the event instance
        messages.success(request, 'Event deleted successfully!')
        return redirect('event_list')  # Redirect to event list after deletion

