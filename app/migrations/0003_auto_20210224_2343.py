# Generated by Django 3.1.6 on 2021-02-24 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210224_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='money',
            name='create_date',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='createddate'),
        ),
    ]
