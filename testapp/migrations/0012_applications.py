# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-23 07:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0011_auto_20171222_2352'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('image', models.CharField(max_length=1000)),
                ('link', models.CharField(max_length=1000)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
    ]
