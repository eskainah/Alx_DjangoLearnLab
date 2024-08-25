from django.urls import path , include
from .views import UserLoginView, UserLogoutView, UserRegisterView,list_books, LibraryDetailView , home
from . import views
urlpatterns = [
      path('add_book/', views.AddBookView.as_view(), name='add_book'),
    path('edit_book/<int:pk>/', views.EditBookView.as_view(), name='edit_book'),
    path('delete_book/<int:pk>/', views.DeleteBookView.as_view(), name='delete_book'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('', home, name='home'),  # Root URL
     path('books/', list_books, name='list_books'),  # URL pattern for the function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL pattern for the class-based view
]