from django.shortcuts import render
from django.db.models import Q

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import UserPassesTestMixin

from django.contrib.auth.models import User
from  .forms import CustomUserCreationForm
from .forms import CustomUserChangeForm
from .models import Post, Comment

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
    

class NewPost(CreateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = '__all__'
    success_url = "/posts"


class Posts(ListView):
    model = Post
    template_name = "blog/post_list.html"


class PostDetail(DetailView):
    model = Post
    template_name = "blog/posts_detail.html"


class PostEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "blog/update_post.html"
    fields = '__all__'
    success_url = "/posts"

    def handle_no_permission(self):
        return redirect('login')


class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/delete_post.html"
    success_url = "/posts"

    def handle_no_permission(self):
        return redirect('login')
    
class CommentUpdateView(UpdateView):
    model = Comment
    template_name = "blog/post_detail.html"
    fields = '__all__'
    success_url = "/posts"

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = "blog/post_detail.html"
    success_url = "/posts"

class CommentCreateView(CreateView):
    model = Post
    template_name = "blog/post_detail.html"
    fields = '__all__'
    success_url = "/posts"


def search_posts(request):
    query = request.GET.get('q')  # Get the query from the search form
    results = Post.objects.all()

    if query:
        # Using Q objects to filter by title, content, or tags
        results = Post.objects.filter(
            Q(title__icontains=query) |  # Search by title
            Q(content__icontains=query) |  # Search by content
            Q(tags__name__icontains=query)  # Search by tags (from django-taggit)
        ).distinct()

    return render(request, 'search_results.html', {'results': results, 'query': query})