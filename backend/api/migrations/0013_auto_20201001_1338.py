# Generated by Django 3.1.1 on 2020-10-01 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20201001_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='URL',
            field=models.CharField(max_length=255, null=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='card',
            name='board',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='api.board'),
        ),
        migrations.AlterField(
            model_name='card',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='作成日時'),
        ),
        migrations.AlterField(
            model_name='card',
            name='positionX',
            field=models.IntegerField(null=True, verbose_name='x座標'),
        ),
        migrations.AlterField(
            model_name='card',
            name='positionY',
            field=models.IntegerField(null=True, verbose_name='y座標'),
        ),
        migrations.AlterField(
            model_name='card',
            name='summary',
            field=models.CharField(max_length=500, null=True, verbose_name='サマリー'),
        ),
        migrations.AlterField(
            model_name='card',
            name='thumbnail',
            field=models.CharField(max_length=255, null=True, verbose_name='サムネイル'),
        ),
        migrations.AlterField(
            model_name='card',
            name='title',
            field=models.CharField(max_length=255, null=True, verbose_name='タイトル'),
        ),
        migrations.AlterField(
            model_name='card',
            name='update_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='更新日時'),
        ),
    ]