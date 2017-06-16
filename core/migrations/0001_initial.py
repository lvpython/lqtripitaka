# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 16:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('user_count', models.IntegerField()),
                ('view_count', models.IntegerField()),
            ],
            options={
                'verbose_name': '访问记录',
                'verbose_name_plural': '访问记录',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=64, unique=True, verbose_name='编号')),
                ('name', models.CharField(max_length=64, verbose_name='页码')),
                ('pre_page', models.UUIDField(blank=True, null=True, verbose_name='上一页')),
                ('next_page', models.UUIDField(blank=True, null=True, verbose_name='下一页')),
            ],
            options={
                'verbose_name': '页',
                'verbose_name_plural': '页管理',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PageResource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('TX', '文本'), ('IM', '图片'), ('TN', '插图')], default='TX', max_length=2, verbose_name='类型')),
                ('resource', models.FileField(upload_to='', verbose_name='资源')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Page', verbose_name='页')),
            ],
            options={
                'verbose_name': '页资源',
                'verbose_name_plural': '页资源列表',
            },
        ),
        migrations.CreateModel(
            name='Roll',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=64, unique=True, verbose_name='编号')),
                ('name', models.CharField(max_length=64, verbose_name='卷名')),
                ('page_count', models.IntegerField(blank=True, null=True, verbose_name='页数')),
                ('start_page', models.UUIDField(blank=True, null=True, verbose_name='起始页')),
                ('end_page', models.UUIDField(blank=True, null=True, verbose_name='终止页')),
                ('qianziwen', models.CharField(blank=True, max_length=8, null=True, verbose_name='千字文')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '卷',
                'verbose_name_plural': '卷管理',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=64, unique=True, verbose_name='编号')),
                ('name', models.CharField(max_length=64, verbose_name='版本名')),
                ('type', models.CharField(choices=[('SS', '藏经丛书'), ('OP', '单行本')], default='SS', max_length=2, verbose_name='版本类型')),
                ('volume_count', models.IntegerField(blank=True, null=True, verbose_name='册数')),
                ('sutra_count', models.IntegerField(blank=True, null=True, verbose_name='经数')),
                ('dynasty', models.CharField(blank=True, max_length=64, null=True, verbose_name='朝代')),
                ('historic_site', models.CharField(blank=True, max_length=64, null=True, verbose_name='刻经地点')),
                ('publish_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='出版社')),
                ('publish_date', models.DateField(blank=True, null=True, verbose_name='出版时间')),
                ('publish_edition', models.SmallIntegerField(blank=True, null=True, verbose_name='版次')),
                ('publish_prints', models.SmallIntegerField(blank=True, null=True, verbose_name='印次')),
                ('publish_ISBN', models.CharField(blank=True, max_length=64, null=True, verbose_name='ISBN')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '藏经版本',
                'verbose_name_plural': '藏经版本管理',
            },
        ),
        migrations.CreateModel(
            name='Sutra',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=64, unique=True, verbose_name='编号')),
                ('name', models.CharField(max_length=64, verbose_name='经名')),
                ('type', models.CharField(choices=[('ST', '经'), ('RT', '律'), ('TT', '论')], default='ST', max_length=2, verbose_name='类型')),
                ('clazz', models.CharField(blank=True, max_length=64, null=True, verbose_name='部别')),
                ('dynasty', models.CharField(blank=True, max_length=64, null=True, verbose_name='朝代')),
                ('historic_site', models.CharField(blank=True, max_length=64, null=True, verbose_name='译经地点')),
                ('roll_count', models.IntegerField(blank=True, null=True, verbose_name='卷数')),
                ('start_page', models.UUIDField(blank=True, null=True, verbose_name='起始页')),
                ('end_page', models.UUIDField(blank=True, null=True, verbose_name='终止页')),
                ('qianziwen', models.CharField(blank=True, max_length=8, null=True, verbose_name='千字文')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('series', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Series', verbose_name='版本')),
            ],
            options={
                'verbose_name': '经',
                'verbose_name_plural': '经管理',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Translator',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, verbose_name='作译者名字')),
                ('type', models.CharField(choices=[('TS', '译者'), ('AH', '作者')], default='TS', max_length=2, verbose_name='类型')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '作译者',
                'verbose_name_plural': '作译者管理',
            },
        ),
        migrations.CreateModel(
            name='Volume',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=64, unique=True, verbose_name='编号')),
                ('name', models.CharField(max_length=64, verbose_name='册名')),
                ('start_page', models.UUIDField(blank=True, null=True, verbose_name='起始页')),
                ('end_page', models.UUIDField(blank=True, null=True, verbose_name='终止页')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('series', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Series', verbose_name='版本')),
            ],
            options={
                'verbose_name': '册',
                'verbose_name_plural': '册管理',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='sutra',
            name='translator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Translator', verbose_name='作译者'),
        ),
        migrations.AddField(
            model_name='roll',
            name='series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Series', verbose_name='版本'),
        ),
        migrations.AddField(
            model_name='roll',
            name='sutra',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Sutra', verbose_name='经'),
        ),
        migrations.AddField(
            model_name='page',
            name='roll',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Roll', verbose_name='卷'),
        ),
        migrations.AddField(
            model_name='page',
            name='series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Series', verbose_name='部'),
        ),
        migrations.AddField(
            model_name='page',
            name='sutra',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Sutra', verbose_name='经'),
        ),
        migrations.AddField(
            model_name='page',
            name='volume',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Volume', verbose_name='册'),
        ),
    ]
