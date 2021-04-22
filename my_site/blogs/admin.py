from django.contrib import admin
from blogs.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_at', 'status')
    list_filter = ('status', 'created_at', 'published_at', 'author')
    search_fields = ('title', 'content')
    raw_id_fields = ('author',)
    date_hierarchy = 'published_at'
    ordering = ('status', '-published_at')

admin.site.register(Post, PostAdmin)