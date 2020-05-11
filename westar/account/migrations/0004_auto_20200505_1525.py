# Generated by Django 3.0.5 on 2020-05-05 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20200505_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfeeds',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.User'),
        ),
        migrations.RemoveField(
            model_name='userfeeds',
            name='follows',
        ),
        migrations.AddField(
            model_name='userfeeds',
            name='follows',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='follows', to='account.User'),
        ),
    ]