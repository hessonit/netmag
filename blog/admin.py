from django.contrib import admin
from blog.models import Post
from blog.models import Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_filter = ['published', 'created']
    search_fields = ['title', 'description', 'content']
    date_hierarchy = 'created'
    save_on_top = True
    prepopulated_fields = {"slug": ("title",)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ["post", "author", "created"]

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

