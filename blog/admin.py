from django.contrib import admin
from .models import Post, Comment
# Register your models here.


# @admin.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'publish')
    list_filter = ('created', 'publish', 'author')
    search_fields = ( 'body',)
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ( 'publish',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'created')
    list_filter = ('created', 'updated')
    search_fields = ('email', 'body')