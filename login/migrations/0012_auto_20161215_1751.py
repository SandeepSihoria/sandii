# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-15 17:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_auto_20161215_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='dateof_visit',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 12, 15, 17, 51, 6, 68137, tzinfo=utc)),
        ),
    ]
