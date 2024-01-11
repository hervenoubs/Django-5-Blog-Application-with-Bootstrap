from django.urls import path
from .views import blog_index, blog_detail, blog_category, about, contact, shop
from authentication.views import user_registration

urlpatterns = [
    path('', blog_index, name='blog_index'),
    path('blog/post/<int:pk>/', blog_detail, name='blog_detail'),
    path("blog/category/<str:category_name>/", blog_category, name="blog_category"),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('shop/', shop, name='shop'),
    path('registration/', user_registration, name='user_registration'),
]