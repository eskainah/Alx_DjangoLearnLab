from django.urls import path
from .views import register, login_view, home, event_list, create_event, event_detail, update_event, delete_event

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('', home, name='home'),
    path('event/', event_list, name='event_list'),
    path('events/create/', create_event, name='create_event'),
    path('event/<int:pk>/', event_detail, name='event_detail'),
    path('event/<int:pk>/edit/', update_event, name='update_event'),
    path('event/<int:pk>/delete/', delete_event, name='delete_event'),
]
