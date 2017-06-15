# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-15 00:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20170614_2329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='页码')),
                ('resource', models.CharField(blank=True, max_length=128, verbose_name='资源')),
                ('next_page', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='page_next_page', to='core.Page', verbose_name='下一页')),
                ('pre_page', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='page_pre_page', to='core.Page', verbose_name='上一页')),
            ],
        ),
        migrations.CreateModel(
            name='Roll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='卷名')),
                ('page_count', models.IntegerField(verbose_name='页数')),
                ('qianziwen', models.CharField(max_length=8, verbose_name='千字文')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('end_page', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='roll_end_page', to='core.Page', verbose_name='终止页')),
                ('start_page', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='roll_start_page', to='core.Page', verbose_name='起始页')),
            ],
        ),
        migrations.CreateModel(
            name='Sutra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='经名')),
                ('type', models.CharField(choices=[('ST', '经'), ('RT', '律'), ('TT', '论')], default='ST', max_length=2, verbose_name='类型')),
                ('dynasty', models.CharField(max_length=64, verbose_name='朝代')),
                ('historic_site', models.CharField(max_length=64, verbose_name='刻经地点')),
                ('roll_count', models.IntegerField(verbose_name='卷数')),
                ('qianziwen', models.CharField(max_length=8, verbose_name='千字文')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('end_page', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sutra_end_page', to='core.Page', verbose_name='终止页')),
            ],
        ),
        migrations.AddField(
            model_name='volume',
            name='remark',
            field=models.TextField(blank=True, null=True, verbose_name='备注'),
        ),
        migrations.AddField(
            model_name='volume',
            name='series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Series', verbose_name='版本'),
        ),
        migrations.AlterField(
            model_name='series',
            name='remark',
            field=models.TextField(blank=True, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='translator',
            name='remark',
            field=models.TextField(blank=True, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='translator',
            name='type',
            field=models.CharField(choices=[('TS', '译者'), ('AH', '作者')], default='TS', max_length=2, verbose_name='类型'),
        ),
        migrations.AlterField(
            model_name='volume',
            name='name',
            field=models.CharField(max_length=64, verbose_name='册名'),
        ),
        migrations.AddField(
            model_name='sutra',
            name='series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Series', verbose_name='版本'),
        ),
        migrations.AddField(
            model_name='sutra',
            name='start_page',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sutra_start_page', to='core.Page', verbose_name='起始页'),
        ),
        migrations.AddField(
            model_name='sutra',
            name='translator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Translator', verbose_name='作译者'),
        ),
        migrations.AddField(
            model_name='roll',
            name='sutra',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Sutra', verbose_name='经'),
        ),
        migrations.AddField(
            model_name='page',
            name='roll',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Roll', verbose_name='卷'),
        ),
        migrations.AddField(
            model_name='page',
            name='series',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Series', verbose_name='部'),
        ),
        migrations.AddField(
            model_name='page',
            name='sutra',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Sutra', verbose_name='经'),
        ),
        migrations.AddField(
            model_name='page',
            name='volume',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Volume', verbose_name='册'),
        ),
        migrations.AddField(
            model_name='volume',
            name='end_page',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='volume_end_page', to='core.Page', verbose_name='终止页'),
        ),
        migrations.AddField(
            model_name='volume',
            name='start_page',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='volume_start_page', to='core.Page', verbose_name='起始页'),
        ),
    ]
