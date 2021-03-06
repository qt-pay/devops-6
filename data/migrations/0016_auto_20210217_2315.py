# Generated by Django 3.1.6 on 2021-02-17 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0015_auto_20210217_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guxiaobei',
            name='comment',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='comment'),
        ),
        migrations.AlterField(
            model_name='guxiaobei',
            name='createddate',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='createddate'),
        ),
        migrations.AlterField(
            model_name='guxiaobei',
            name='itemid',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='itemid'),
        ),
        migrations.AlterField(
            model_name='guxiaobei',
            name='keywords',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='keywords'),
        ),
        migrations.AlterField(
            model_name='guxiaobei',
            name='updateddate',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='updateddate'),
        ),
    ]
