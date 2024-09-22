from django.urls import path, include
from .views import PostViewSet, CommentViewSet, FeedView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts',PostViewSet)
router.register(r'comments', CommentViewSet)

posts_url = urlpatterns = router.urls

urlpatterns = [
    path('', include(posts_url)),
    path('feed/', FeedView.as_view(), name='feed'),
]

