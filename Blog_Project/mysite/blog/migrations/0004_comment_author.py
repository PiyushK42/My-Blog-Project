# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-05-23 10:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190522_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.CharField(default='auth.User', max_length=200),
        ),
    ]
