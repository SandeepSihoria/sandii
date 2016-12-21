# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-15 17:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_society'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=100)),
                ('visitor_name', models.CharField(max_length=100)),
                ('visitor_mobile', models.CharField(max_length=100)),
                ('otp', models.CharField(max_length=100)),
                ('flat_id', models.CharField(max_length=10)),
                ('dateof_visit', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
