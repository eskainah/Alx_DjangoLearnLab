from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import CustomUser
from .forms import CustomUserCreationForm  

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
        #register the a new user
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
             #Redirect to homepage
            return redirect('home')
    return render(request, 'accounts/login.html')