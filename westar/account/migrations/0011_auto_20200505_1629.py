# Generated by Django 3.0.5 on 2020-05-05 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20200505_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='followers',
        ),
        migrations.RemoveField(
            model_name='user',
            name='follows',
        ),
        migrations.CreateModel(
            name='Follow_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follows', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='follows', to='account.User')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.User')),
            ],
        ),
        migrations.AddField(
            model_name='userfeeds',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='user_followers', to='account.Follow_user'),
        ),
    ]
