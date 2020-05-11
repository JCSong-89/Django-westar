from django.contrib import admin

from . import models

# Register your models here.

@admin.register(models.Content)
class CustomPostAdmin(admin.ModelAdmin):
    list_display = ("user_id", "description", "createdAt")


@admin.register(models.Comments)
class CustomCommentsAdmin(admin.ModelAdmin):
    list_display = ("user_id", "content_id", "comment", "createdAt", "updatedAt")


@admin.register(models.Like)
class CustomLikesAdmin(admin.ModelAdmin):
    list_display = ("user_id", "content_id", "isLike")


