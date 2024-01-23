from django.urls import path
from .views import create_post, manage_posts, delete_post, edit_post, update_post

urlpatterns = [
    path('create/', create_post, name='create_post'),
    path('posts/', manage_posts, name='manage_posts'),
    path('delete/<int:pk>/', delete_post, name='delete_post'),
    path('edit-post/<int:pk>/', edit_post, name='edit_post'),
    path('update/<int:pk>/', update_post, name='update_post'),
]