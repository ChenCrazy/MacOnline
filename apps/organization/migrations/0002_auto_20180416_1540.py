# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-16 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='image',
            field=models.ImageField(default='', upload_to='author/%Y/%m', verbose_name='头像'),
        ),
    ]
