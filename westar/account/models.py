from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=128, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)    
    telephone = models.IntegerField(unique=True)
    avartar = models.URLField(blank=True)
    bio = models.TextField(default="", blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    following = models.ManyToManyField('self', through='Follow', symmetrical=False)

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'users'

class Follow(models.Model):
    follow = models.ForeignKey('User', on_delete=models.SET_NULL, related_name="follow", null=True)
    follower = models.ForeignKey('User', on_delete=models.SET_NULL, related_name="follower", null=True)

    class Meta:
        db_table = 'follows'