from django.db import models

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
    categories = models.ManyToManyField("Category", related_name="posts")
    post_slug = models.SlugField(unique=True)
    post_intro = models.TextField(default='')
    post_content = models.TextField()
    post_banner = models.ImageField(upload_to='images')  
    created_on = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.post_title

class Comments(models.Model):
    visitor_name = models.CharField(max_length=60)
    visitor_comment = models.TextField()
    visitor_email = models.EmailField(max_length=254, unique=True, default='')
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

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