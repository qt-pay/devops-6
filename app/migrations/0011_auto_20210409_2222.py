# Generated by Django 3.1.6 on 2021-04-09 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20210409_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jenkins',
            name='duration',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='耗时(s)'),
        ),
    ]
