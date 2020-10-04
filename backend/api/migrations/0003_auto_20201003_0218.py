# Generated by Django 3.1.1 on 2020-10-03 02:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_auto_20201003_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='comments',
            field=models.ManyToManyField(related_name='comments', through='api.Comment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='board',
            name='likes',
            field=models.ManyToManyField(related_name='likes', through='api.Like', to=settings.AUTH_USER_MODEL),
        ),
    ]