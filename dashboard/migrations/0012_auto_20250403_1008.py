# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2025-04-03 10:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_universityrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='universityrequest',
            name='university_name',
            field=models.CharField(choices=[('andhra', 'Andhra'), ('bharathidasan', 'Bharathidasan'), ('chandigarh', 'Chandigarh'), ('centurion', 'Centurion'), ('drmgr', 'DrMGR'), ('dypatil', 'DYPatil'), ('jain', 'Jain'), ('kiit', 'KIIT'), ('kuk', 'KUK'), ('vgu', 'VGU'), ('niu', 'NIU'), ('jnu', 'JNU'), ('atlas', 'Atlas')], max_length=255),
        ),
    ]
