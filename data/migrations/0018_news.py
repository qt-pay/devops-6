# Generated by Django 3.1.6 on 2021-02-17 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0017_auto_20210217_2348'),
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemid', models.BigIntegerField(blank=True, null=True, verbose_name='itemid')),
                ('title', models.CharField(max_length=500, null=True, verbose_name='title')),
                ('link', models.CharField(max_length=500, null=True, verbose_name='link')),
                ('type', models.CharField(max_length=50, null=True, verbose_name='type')),
                ('subtype', models.CharField(max_length=50, null=True, verbose_name='subtype')),
                ('star', models.IntegerField(default=0)),
                ('sent', models.IntegerField(default=0)),
                ('checked', models.BooleanField(default=False, verbose_name='checked')),
                ('keywords', models.CharField(blank=True, max_length=50, null=True, verbose_name='keywords')),
                ('comment', models.CharField(blank=True, max_length=2000, null=True, verbose_name='comment')),
                ('createddate', models.CharField(blank=True, max_length=200, null=True, verbose_name='createddate')),
                ('updateddate', models.CharField(blank=True, max_length=200, null=True, verbose_name='updateddate')),
            ],
            options={
                'verbose_name': 'news',
                'verbose_name_plural': '消息集合',
            },
        ),
    ]