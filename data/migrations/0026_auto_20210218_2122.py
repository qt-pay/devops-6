# Generated by Django 3.1.6 on 2021-02-18 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0025_auto_20210218_2120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fuyuzhe',
            old_name='type',
            new_name='subtype',
        ),
    ]