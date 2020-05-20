from django.db import models

from account import models as USER_MODELS
# Create your models here.

class Photo(models.Model):
    content = models.ForeignKey('Content', on_delete=models.SET_NULL, null=True)
    image_file  = models.URLField()
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'photos'

class Content(models.Model):
    user = models.ForeignKey(USER_MODELS.User, on_delete=models.CASCADE)
    description = models.TextField(default="", blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    comment = models.ManyToManyField(USER_MODELS.User, through='Comments', related_name = 'content_comment')
    like = models.ManyToManyField(USER_MODELS.User, through='Like', related_name='like')

    class Meta:
        db_table = 'contents'

class Comments(models.Model):
    user = models.ForeignKey(USER_MODELS.User, on_delete=models.CASCADE)
    content = models.ForeignKey('Content', on_delete=models.CASCADE, null=True)
    comment = models.TextField(blank=True, default="")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'comments'


class Like(models.Model):
    isLike = models.BooleanField(default=False,)
    user = models.ForeignKey(USER_MODELS.User, on_delete=models.CASCADE, related_name='user_like')
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='content_like')

    class Meta:
        db_table = 'likes'

