# Generated by Django 3.1.6 on 2021-02-17 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_auto_20210217_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fuyuzhe',
            name='order',
        ),
        migrations.RemoveField(
            model_name='fuyuzhe',
            name='url',
        ),
        migrations.AddField(
            model_name='fuyuzhe',
            name='comment',
            field=models.CharField(max_length=2000, null=True, verbose_name='comment'),
        ),
        migrations.AddField(
            model_name='fuyuzhe',
            name='createddate',
            field=models.DateTimeField(auto_now=True, verbose_name='createddate'),
        ),
        migrations.AddField(
            model_name='fuyuzhe',
            name='sent',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='fuyuzhe',
            name='star',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='fuyuzhe',
            name='type',
            field=models.CharField(max_length=50, null=True, verbose_name='type'),
        ),
        migrations.AddField(
            model_name='fuyuzhe',
            name='updateddate',
            field=models.DateTimeField(auto_now=True, verbose_name='updateddate'),
        ),
    ]