# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-20 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_auto_20171220_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(upload_to='pic_folder/'),
        ),
    ]
