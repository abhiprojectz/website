# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-12-19 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0132_auto_20181216_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='roundpage',
            name='week_three_stuck_chat_url',
            field=models.URLField(blank=True, verbose_name="URL of the week three chat on what we're stuck on"),
        ),
    ]
