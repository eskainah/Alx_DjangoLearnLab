from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('', list_books, name='list_books'),
    path('', LibraryDetailView.as_view(), name='library_detail'),
    "LogoutView.as_view(template_name="logut.html, 
    "LoginView.as_view(template_name="login.html"
    "views.register"
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view')
]
