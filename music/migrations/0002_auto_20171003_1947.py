# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='Song_tittle',
            new_name='song_tittle',
        ),
        migrations.AddField(
            model_name='song',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
