# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-06 17:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opinion', '0006_auto_20160706_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='tag_lang',
        ),
    ]
