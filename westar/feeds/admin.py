from django.contrib import admin

from . import models
# Register your models here.

class UserFeedAdmin(admin.ModelAdmin):
    list_display = ["user_id"]

admin.site.register(models.UserFeeds, UserFeedAdmin)
