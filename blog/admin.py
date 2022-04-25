from django.contrib import admin
from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'datetime_created', 'datetime_edited']
    ordering = ['datetime_created']
# admin.site.register(BlogPost, BlogPostAdmin)
