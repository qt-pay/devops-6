# Generated by Django 3.1.6 on 2021-02-17 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0019_delete_zhihu'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'zhihu', 'verbose_name_plural': '知乎'},
        ),
    ]
