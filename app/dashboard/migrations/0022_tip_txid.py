# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-02 00:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0021_tip_network'),
    ]

    operations = [
        migrations.AddField(
            model_name='tip',
            name='txid',
            field=models.CharField(default='', max_length=255),
        ),
    ]
