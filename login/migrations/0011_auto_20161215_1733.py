# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-15 17:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_visitor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='dateof_visit',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
