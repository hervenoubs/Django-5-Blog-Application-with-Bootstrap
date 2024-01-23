from django.urls import path
from .views import user_registration, user_login, user_logout, home
from accounts.views import create_post, manage_posts

urlpatterns = [
    path('registration/', user_registration, name='registration'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('home/', home, name='home'),
    path('create/', create_post, name='create_post'),
    path('posts/', manage_posts, name='manage_posts'),
]