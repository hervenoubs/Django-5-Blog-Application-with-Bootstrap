from django.urls import path
from .views import create_post, manage_posts, delete_post, edit_post, update_post, post_comments, approve_post, disapprove_post

urlpatterns = [
    path('create/', create_post, name='create_post'),
    path('posts/', manage_posts, name='manage_posts'),
    path('delete/<int:pk>/', delete_post, name='delete_post'),
    path('edit-post/<int:pk>/', edit_post, name='edit_post'),
    path('update/<int:pk>/', update_post, name='update_post'),
    path('comments/', post_comments, name='post_comments'),
    path('approve-comment/<int:pk>/', approve_post, name='approve_post'),
    path('disapprove-comment/<int:pk>/', disapprove_post, name='disapprove_post'),
]