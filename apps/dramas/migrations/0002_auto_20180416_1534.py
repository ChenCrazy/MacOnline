# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-16 15:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dramas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='serial',
            options={'verbose_name': '剧集', 'verbose_name_plural': '剧集'},
        ),
        migrations.RenameField(
            model_name='dramaresource',
            old_name='course',
            new_name='drama',
        ),
        migrations.RenameField(
            model_name='serial',
            old_name='course',
            new_name='drama',
        ),
        migrations.AddField(
            model_name='drama',
            name='is_banner',
            field=models.BooleanField(default=False, verbose_name='是否轮播'),
        ),
        migrations.AlterField(
            model_name='drama',
            name='image',
            field=models.ImageField(upload_to='dramas/%Y/%m', verbose_name='封面图'),
        ),
        migrations.AlterField(
            model_name='dramaresource',
            name='download',
            field=models.FileField(upload_to='dramas/resource/%Y/%m', verbose_name='资源文件'),
        ),
        migrations.AlterField(
            model_name='video',
            name='serial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dramas.Serial', verbose_name='剧集'),
        ),
    ]
