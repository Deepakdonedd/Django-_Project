# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2025-04-02 06:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20250402_0553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='ticket_em_cc',
        ),
        migrations.AddField(
            model_name='ticket',
            name='ticket_em_cc',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
