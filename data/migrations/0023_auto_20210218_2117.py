# Generated by Django 3.1.6 on 2021-02-18 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0022_auto_20210218_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zhihu',
            name='subtype',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='subtype'),
        ),
        migrations.AlterField(
            model_name='zhihu',
            name='type',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='type'),
        ),
    ]
