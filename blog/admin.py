from django.contrib import admin
from .models import Post, Author, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ("title","date","author")
    list_filter = ("author","date","tags")
    prepopulated_fields = {"slug": ("title",)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ("username","post")
    

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
