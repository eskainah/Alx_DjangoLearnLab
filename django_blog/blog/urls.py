from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import Register, Login, ProfileView, NewPost, Posts, PostDetail, PostEdit, PostDelete, \
                    CommentUpdateView, CommentCreateView, CommentDeleteView, search_posts, PostByTagListView

urlpatterns = [
    path('register/', Register.as_view(), name="regiser"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('profile/', ProfileView, name="profile"),

    path('posts/', Posts.as_view(), name="posts"),
    path('posts/<int:pk>/', PostDetail.as_view(), name="post_detail"),
    path('post/<int:pk>/update/', PostEdit.as_view(), name="post_edit"),
    path('post/new/', NewPost.as_view(), name='new_post'),
    path('post/<int:pk>/delete/', PostDelete.as_view(), name="post_delete"),

    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name="comment_update"),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name="create_comment"),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name="delete"),

    path('search/', search_posts, name='search_posts'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts_by_tag'),  # New URL for filtering by tag
]