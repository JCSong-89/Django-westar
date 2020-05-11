from django.db import models

from account import models as USER_MODELS
# Create your models here.

class Photo(models.Model):
    image_file  = models.ImageField()
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'photo'

class Content(models.Model):
    user_id = models.ForeignKey(USER_MODELS.User, on_delete=models.CASCADE)
    description = models.TextField(default="", blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    images = models.ManyToManyField(Photo)

    class Meta:
        db_table = 'content'

class Comments(models.Model):
    user_id = models.ForeignKey(USER_MODELS.User, on_delete=models.CASCADE)
    content_id = models.OneToOneField(Content, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comments'

class Like(models.Model):
    isLike = models.BooleanField(default=False,)
    user_id = models.ForeignKey(USER_MODELS.User, on_delete=models.CASCADE)
    content_id = models.ForeignKey(Content, on_delete=models.CASCADE)

    class Meta:
        db_table = 'like'