from django.contrib import admin
from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    # fields = [
    #     'title',
    #     'content',
    #     'image'
    # ]

    fieldsets = ('title', {'fields': ['title', 'created_at']}), ('content', {
        'fields': ['content', 'image']})


admin.site.register(BlogPost, BlogPostAdmin)
