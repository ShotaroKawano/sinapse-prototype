# Generated by Django 3.1.1 on 2020-09-25 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200924_1607'),
    ]

    operations = [
        migrations.RenameField(
            model_name='arrows',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='arrows',
            old_name='update_date',
            new_name='update_at',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='update_date',
            new_name='update_at',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='update_date',
            new_name='update_at',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='board',
            new_name='board_id',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='user',
            new_name='user_id',
        ),
        migrations.RemoveField(
            model_name='like',
            name='update_date',
        ),
    ]
