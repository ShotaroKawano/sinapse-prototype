# Generated by Django 3.1.1 on 2020-10-07 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201005_0513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='thumbnail',
            field=models.CharField(max_length=2083),
        ),
        migrations.AlterField(
            model_name='card',
            name='url',
            field=models.CharField(max_length=2083),
        ),
    ]
