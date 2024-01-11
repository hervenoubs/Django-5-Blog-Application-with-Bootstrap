from django.contrib import admin
from .models import Post, Comments, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'created_on', 'modified_at')

class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'post_slug', 'post_intro', 'post_banner', 'created_on', 'modified_at')

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('visitor_name', 'visitor_comment', 'created_on', 'post')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comments, CommentsAdmin)

