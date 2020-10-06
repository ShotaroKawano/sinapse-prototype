# Generated by Django 3.1.1 on 2020-10-05 05:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='comments1',
            field=models.ManyToManyField(related_name='comments2', through='api.Comment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='board',
            name='likes',
            field=models.ManyToManyField(related_name='likes', through='api.Like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='board',
            name='tags',
            field=models.ManyToManyField(related_name='tags', through='api.Board_Tag', to='api.Tag'),
        ),
        migrations.AddField(
            model_name='card',
            name='arrows',
            field=models.ManyToManyField(related_name='_card_arrows_+', through='api.Arrow', to='api.Card'),
        ),
    ]