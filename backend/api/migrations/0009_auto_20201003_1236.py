# Generated by Django 3.1.1 on 2020-10-03 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20201003_0333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.AddField(
            model_name='arrow',
            name='from_position',
            field=models.CharField(default='top', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='arrow',
            name='to_position',
            field=models.CharField(default='top', max_length=255),
            preserve_default=False,
        ),
    ]