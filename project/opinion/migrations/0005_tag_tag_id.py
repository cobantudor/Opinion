# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-06 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opinion', '0004_auto_20160706_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='tag_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
