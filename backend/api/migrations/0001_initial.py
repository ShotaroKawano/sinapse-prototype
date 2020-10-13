# Generated by Django 3.1.1 on 2020-10-13 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Arrow_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('thumbnail', models.CharField(blank=True, max_length=255, null=True)),
                ('url_tail', models.CharField(blank=True, max_length=255, null=True)),
                ('is_published', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_boards', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_likes', to='api.board')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_comments', to='api.board')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=2083)),
                ('title', models.CharField(max_length=255)),
                ('summary', models.TextField(blank=True, null=True)),
                ('thumbnail', models.CharField(blank=True, max_length=2083, null=True)),
                ('position_x', models.IntegerField()),
                ('position_y', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_cards', to='api.board')),
            ],
        ),
        migrations.CreateModel(
            name='Board_Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_tags', to='api.board')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag_boards', to='api.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Arrow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_position', models.CharField(max_length=255)),
                ('to_position', models.CharField(max_length=255)),
                ('label', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('arrow_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.arrow_type')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_arrows', to='api.board')),
                ('from_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_from_cards', to='api.card')),
                ('to_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_to_cards', to='api.card')),
            ],
        ),
    ]
