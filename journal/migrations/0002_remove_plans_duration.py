# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-17 16:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plans',
            name='duration',
        ),
    ]
