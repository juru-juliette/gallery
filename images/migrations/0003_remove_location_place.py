# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-13 15:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20191011_1222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='place',
        ),
    ]