# Generated by Django 3.1.6 on 2021-02-17 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0011_zhihu_checked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zhihu',
            name='createddate',
            field=models.DateTimeField(verbose_name='createddate'),
        ),
        migrations.AlterField(
            model_name='zhihu',
            name='updateddate',
            field=models.DateTimeField(verbose_name='updateddate'),
        ),
    ]
