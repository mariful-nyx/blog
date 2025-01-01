from django.contrib import admin
from bpm.post.models import Post, Like
# Register your models here.


admin.site.register(Like)

class ModelPost(admin.ModelAdmin):
    list_display = ['id', 'title']
admin.site.register(Post, ModelPost)
