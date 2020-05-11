from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=128, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)    
    telephone = models.IntegerField(unique=True)
    avartar = models.ImageField(blank=True)
    bio = models.TextField(default="", blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'


