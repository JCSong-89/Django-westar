from django.contrib import admin

from . import models

# Register your models here.

class CustomPostAdmin(admin.ModelAdmin):
    #list_display = ("user", "description", "createdAt")
    pass
@admin.register(models.Comments)
class CustomCommentsAdmin(admin.ModelAdmin):
    list_display = ("comment", "content", 'user')

admin.site.register(models.Content, CustomPostAdmin)

@admin.register(models.Like)
class CustomLikesAdmin(admin.ModelAdmin):
    list_display = ("user", "content", "isLike")

@admin.register(models.Photo)
class CustomPhoto(admin.ModelAdmin):
    list_display = ['id', 'image_file', 'createdAt' ,'content']

