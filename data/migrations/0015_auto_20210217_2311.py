# Generated by Django 3.1.6 on 2021-02-17 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0014_guxiaobei'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guxiaobei',
            name='keywords',
            field=models.CharField(max_length=50, null=True, verbose_name='keywords'),
        ),
    ]
