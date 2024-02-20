from django.contrib import admin

from .models import Post, Comment, LikeModel, DislikeModel
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(LikeModel)
admin.site.register(DislikeModel)
