# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 07:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shadowsocks', '0010_auto_20170831_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='level_expire_time',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='等级有效期', verbose_name='等级有效期'),
        ),
    ]