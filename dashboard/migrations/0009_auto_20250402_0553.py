# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2025-04-02 05:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20250401_1750'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='ticket_summary',
            new_name='ticket_subject',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='project',
        ),
    ]
