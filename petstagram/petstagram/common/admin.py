from django.contrib import admin
from petstagram.common.models import CommentText, Like


# Register your models here.

@admin.register(CommentText)
class CommentTextAdmin(admin.ModelAdmin):
    pass


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass
