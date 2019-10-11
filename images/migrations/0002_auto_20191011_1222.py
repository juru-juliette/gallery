# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-11 12:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='category',
            field=models.ForeignKey(db_column='category', on_delete=django.db.models.deletion.CASCADE, to='images.Category'),
        ),
    ]
