from django.urls import path  # Import 'path'
from . import views  # Import views from the current directory
from django.contrib.auth import views as auth_views  # Import auth views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # Main task list page
    path('register/', views.register, name='register'),  # Register page
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Login page
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout page
    path('add/', views.add_task, name='add_task'),  # Add task page
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),  # Edit task page
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),  # Delete task page
    path('view/<int:task_id>/', views.view_task, name='view_task'),  # View task page
]





