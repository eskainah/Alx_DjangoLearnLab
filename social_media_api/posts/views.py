from rest_framework import viewsets, permissions
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import generics

from .models import Post, Comment, Like
from notifications.models import Notification
from .serializers import PostSerializer, CommentSerializer



class PostViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        following_users = user.following.all()
        Post.objects.filter(author__in=following_users).order_by
        posts = Post.objects.filter(
            author__in=following_users).order_by('-created_at')
        serialized_posts = PostSerializer(posts, many=True)
        return Response(serialized_posts.data)

class LikePostView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            # create notification
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post
            )
            return Response({'status': 'liked'}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'already_liked'}, status=status.HTTP_400_BAD_REQUEST)


class UnlikePostView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):

        post = get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(user=request.user, post=post).first()
        if like:
            like.delete()
            return Response({'status': 'unliked'}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'not liked'}, status=status.HTTP_400_BAD_REQUEST)