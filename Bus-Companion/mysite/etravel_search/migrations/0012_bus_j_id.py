# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-22 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etravel_search', '0011_passenger'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='J_ID',
            field=models.CharField(default=0, max_length=8),
            preserve_default=False,
        ),
    ]