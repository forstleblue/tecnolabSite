# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-01 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sito', '0004_auto_20160901_0749'),
    ]

    operations = [
        migrations.AddField(
            model_name='stand',
            name='link',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]