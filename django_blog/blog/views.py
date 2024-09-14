from django.shortcuts import render

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import UserPassesTestMixin

from django.contrib.auth.models import User
from  .forms import CustomUserCreationForm
from .forms import CustomUserChangeForm
from .models import Post

from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from django.urls import reverse 
# Create your views here.
class Register(CreateView):
    form_class = CustomUserCreationForm
    template_name = "blog/register.html"
    template_name_suffix = "form"
    success_url = '/profile'

class Login(LoginView):
    template_name = 'blog/login.html'

@login_required
def ProfileView(request):
    user = request.user

    if request.method =="POST":
        form = CustomUserChangeForm(request.POST, instance = user)
        if form.is_valid():
            form.save()
            redirect('profile')
        else:
            form = CustomUserChangeForm(instance = user)
        return render(request, "blog/profile.html", {'form': form})