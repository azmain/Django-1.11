# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-09 19:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]
