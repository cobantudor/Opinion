# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-06 18:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opinion', '0008_remove_tag_tag_cont'),
    ]

    operations = [
        migrations.RenameField(
            model_name='opinion',
            old_name='article',
            new_name='id_article',
        ),
        migrations.RenameField(
            model_name='opinion',
            old_name='author',
            new_name='id_author',
        ),
    ]