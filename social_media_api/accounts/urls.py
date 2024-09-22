from django.urls import path, include
from .views import RegisterView, LoginView, Follow_Unfollow_UserView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='user_registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('follow-unfollow/<int:user_id>/', Follow_Unfollow_UserView.as_view(), name='follow_unfollow_user'),
]