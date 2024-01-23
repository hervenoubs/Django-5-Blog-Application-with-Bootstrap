from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.utils.text import slugify

class Category(models.Model):
    category_name = models.CharField(max_length=70, unique=True)
    created_on = models.DateField()
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "categories"
    
    def __str__(self):
        return self.category_name

class Post(models.Model):
    post_title = models.CharField(max_length=255, unique=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=4)
    categories = models.ManyToManyField("Category", related_name="posts")
    post_slug = AutoSlugField(populate_from='post_title', unique=True, editable=True)
    post_intro = models.TextField(default='')
    post_status = models.BooleanField(default=False)
    post_content = models.TextField()
    post_banner = models.ImageField(upload_to='images')  
    created_on = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.post_title
    
    def save(self, *args, **kwargs):
        # Generate the slug when saving the model
        self.post_slug = slugify(self.post_title)
        super().save(*args, **kwargs)

class Comments(models.Model):
    visitor_name = models.CharField(max_length=60)
    visitor_comment = models.TextField()
    visitor_email = models.EmailField(max_length=254, unique=True, default='')
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.visitor_name} on '{self.post}'"

class Contacts(models.Model):
    name = models.CharField(max_length=155)
    email = models.EmailField(max_length=254, unique=True)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Newsletter(models.Model):
    firstname = models.CharField(max_length=155)
    email = models.EmailField(max_length=255, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email