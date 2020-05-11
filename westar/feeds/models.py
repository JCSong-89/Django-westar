from django.db import models

from account import models as USER_MODELS
from posts import models as CONTENTS_MODELS


# Create your models here.
class UserFeeds(models.Model):
    user_id = models.ForeignKey(USER_MODELS.User, on_delete=models.CASCADE, null=True)
    following = models.ManyToManyField(USER_MODELS.User, related_name="follower", blank=True)
    content_id = models.ManyToManyField(CONTENTS_MODELS.Content, blank=True)

    class Meta:
        db_table = 'userFeeds'

#    def followCount(self):
#        follow = self.objects.filter(follwing).count()
#        return follow 
#    def followerCount(self):
#        follower = self.objects.filter(follower).count()
#        return follower
#    def contentCount(self):
#        content_count = self.objects.all().count
#        return content_count