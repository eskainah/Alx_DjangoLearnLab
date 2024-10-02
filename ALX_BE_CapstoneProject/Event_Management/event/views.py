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

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event created successfully!')
            return redirect('event/home')  # Redirect to home or event list
        else:
            messages.error(request, 'There was an error creating the event.')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})

# View the list of events
def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

# View event details
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})

def update_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully!')
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'events/event_form.html', {'form': form})

def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event deleted successfully!')
        return redirect('event_list')
    return render(request, 'events/event_confirm_delete.html', {'event': event})