# Generated by Django 3.1.1 on 2020-09-29 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200927_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='description',
            field=models.CharField(max_length=500, null=True, verbose_name='ディスクリプション'),
        ),
        migrations.AlterField(
            model_name='board',
            name='thumbnail',
            field=models.CharField(max_length=255, null=True, verbose_name='サムネイル'),
        ),
        migrations.AlterField(
            model_name='board',
            name='title',
            field=models.CharField(max_length=255, null=True, verbose_name='タイトル'),
        ),
        migrations.AlterField(
            model_name='board',
            name='url_tail',
            field=models.CharField(max_length=255, null=True, verbose_name='テイル'),
        ),
    ]