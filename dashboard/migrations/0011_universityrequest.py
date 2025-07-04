# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2025-04-02 09:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0010_auto_20250402_0630'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_name', models.CharField(max_length=255)),
                ('size', models.CharField(choices=[('t4g.small', 't4g.small'), ('t4g.medium', 't4g.medium'), ('t4g.large', 't4g.large')], max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
