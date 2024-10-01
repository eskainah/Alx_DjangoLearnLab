from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .models import CustomUser, Event
from event.forms import CustomUserCreationForm, EventForm
from django.contrib import messages

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