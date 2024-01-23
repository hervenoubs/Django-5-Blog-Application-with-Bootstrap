from django.urls import path
from .views import blog_index, blog_detail, blog_category, about, contact, shop, search
from authentication.views import user_registration, home, user_logout, user_login
from accounts.views import edit_post, update_post, delete_post

urlpatterns = [
    path('', blog_index, name='blog_index'),
    path('blog/post/<int:pk>/', blog_detail, name='blog_detail'),
    path("blog/category/<str:category_name>/", blog_category, name="blog_category"),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('shop/', shop, name='shop'),
    path('search/', search, name='search'),
    path('registration/', user_registration, name='user_registration'),
    path('login/', user_login, name='user_login'),
    path('home/', home, name='home'),
    path('logout/', user_logout, name='user_logout'),
    path('edit-post/<int:pk>/', edit_post, name='edit_post'),
    path('update/<int:pk>/', update_post, name='update_post'),
    path('delete/<int:pk>/', delete_post, name='delete_post'),
]