from django.contrib import admin
from blog.models import Comment, Post, Tag

class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}

admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)