# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-22 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_loci', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='is_mobile',
            field=models.BooleanField(db_index=True, default=False, verbose_name='is mobile?'),
        ),
    ]