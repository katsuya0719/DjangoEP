# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='html',
            name='project',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
