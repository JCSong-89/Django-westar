# Generated by Django 3.0.5 on 2020-05-18 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_remove_like_islike'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='isLike',
            field=models.BooleanField(default=False),
        ),
    ]
