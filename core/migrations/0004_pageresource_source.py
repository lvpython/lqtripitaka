# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20170618_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='pageresource',
            name='source',
            field=models.CharField(choices=[('cbeat', 'cbeta采集'), ('hand', '图片'), ('net', '网络采集')], default='hand', max_length=8, verbose_name='来源'),
        ),
    ]