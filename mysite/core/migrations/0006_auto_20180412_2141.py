# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-04-12 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180412_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document_id',
            field=models.BigIntegerField(default=1, primary_key=True, serialize=False),
        ),
    ]
