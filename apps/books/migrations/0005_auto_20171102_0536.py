# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 05:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_booklist'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default='No description avialable', max_length=6000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='pdf',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='photo',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 2, 5, 34, 37, 387254)),
        ),
        migrations.AlterField(
            model_name='catagory',
            name='name',
            field=models.CharField(max_length=160),
        ),
    ]
