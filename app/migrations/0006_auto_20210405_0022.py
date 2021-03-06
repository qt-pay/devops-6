# Generated by Django 3.1.6 on 2021-04-04 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_jenkins'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jenkins',
            name='building',
            field=models.BooleanField(default=False, null=True, verbose_name='是否构建中'),
        ),
        migrations.AlterField(
            model_name='jenkins',
            name='inQueue',
            field=models.BooleanField(default=False, null=True, verbose_name='排队中'),
        ),
    ]
