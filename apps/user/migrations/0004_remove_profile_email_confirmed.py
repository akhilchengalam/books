# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 09:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20171030_0616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email_confirmed',
        ),
    ]
