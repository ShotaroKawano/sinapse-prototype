# Generated by Django 3.1.1 on 2020-10-01 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20201001_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arrow',
            name='label',
            field=models.CharField(max_length=255, verbose_name='ラベル'),
        ),
        migrations.AlterField(
            model_name='arrow_type',
            name='type',
            field=models.CharField(max_length=255, verbose_name='アロータイプ'),
        ),
    ]
