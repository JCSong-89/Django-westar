# Generated by Django 3.0.5 on 2020-05-05 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_auto_20200505_1717'),
        ('posts', '0002_auto_20200505_1717'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='UserFeeds',
        ),
    ]